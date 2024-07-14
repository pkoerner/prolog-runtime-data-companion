:- use_module(library(avl)).
:- use_module(library(assoc)).
:- use_module(library(mutdict)).
:- use_module(library(mutarray)).
:- use_module(library(logarr)).
:- use_module(library(ordsets)).
:- use_module(library(random)).
:- use_module(library(lists)).
:- use_module(library(file_systems)).

/**********
 * Random *
 **********/
randomseed(42).
%randomseed(1234).

/********
 * Main *
 ********/
main:-
        run_benchmarks_from_file('benchmarks_integer.txt'),
        run_benchmarks_from_file('benchmarks_atoms.txt'),
        run_benchmarks_from_file('benchmarks_complex.txt'),
        run_benchmarks_from_file('benchmarks_avl_fchk.txt'),
        % run_benchmarks_from_file('benchmarks_randomseed1234.txt'). % randomseed needs to be changed manually
        run_benchmarks_from_file('benchmarks_orderedset1_10_100.txt').

run_benchmarks_from_file(BenchFile):-
        open(BenchFile, read, Stream),
        read_file_benchmarks(Stream, BenchInfos),
        close(Stream),
        run_benchmarks_with_bench_infos(BenchInfos).

read_file_benchmarks(Stream, []):-
        at_end_of_stream(Stream).

read_file_benchmarks(Stream, [X|L]):-
        \+ at_end_of_stream(Stream),
        read(Stream,X),
        read_file_benchmarks(Stream,L).

run_benchmarks_with_bench_infos(BenchInfos):-
        findall(_,
                (
                    member(bench_info(BenchInfo), BenchInfos),
                    BenchCall =.. [bench|BenchInfo],
                    call(BenchCall)
                ), _).
        
/********
 * Util * 
 ********/
% Empty loop
% Used to compare runtimes
empty_loop([]).
empty_loop([_|T]):-
        empty_loop(T).

empty_loop10([]).
empty_loop10([_,_,_,_,_,_,_,_,_,_|T]):-
        empty_loop10(T).

steps(LowerBound, UpperBound, _, LowerBound):-
        LowerBound =< UpperBound.
steps(LowerBound, UpperBound, Step, X):-
        LowerBound2 is LowerBound + Step,
        !,
        LowerBound2 =< UpperBound,
        steps(LowerBound2, UpperBound, Step, X).

% Builds file name as a combination of the used predicates.
build_filename(FileDirectory, Predicates, FileNameAddon, FileName):-
        atom_codes('__', Underscores),
        atom_codes(FileDirectory, Prefix),
        atom_codes('.csv', FileExtension),
        atom_codes(FileNameAddon, FileNameAddonCodes),
        
        findall(X,
                (
                    member(Pred, Predicates),
                    atom_codes(Pred, Codes),
                    append([Codes, Underscores], X)                  
                ), Content),
        
        append(Content, ContentFlattened),
        append([Prefix, ContentFlattened, FileNameAddonCodes, FileExtension], L),
   
        atom_codes(FileName, L).

build_directory(FileDirectory):-
        directory_exists(FileDirectory), !.
build_directory(FileDirectory):-
        make_directory(FileDirectory), !.

% Generates Complex Terms
rancomplexterm(Seed, Complex):-
        % Reset random
        setrand(Seed),

        random(97, 123, AsciiCodeLowerCaseLetterInner),
        random(97, 123, AsciiCodeLowerCaseLetterOuter),
        
        atom_codes(term_, PrefixCodes),
        append([PrefixCodes, [AsciiCodeLowerCaseLetterInner]], ComplexNameCodesInner),
        append([PrefixCodes, [AsciiCodeLowerCaseLetterOuter]], ComplexNameCodesOuter),
        atom_codes(ComplexNameInner, ComplexNameCodesInner),
        atom_codes(ComplexNameOuter, ComplexNameCodesOuter),

        append([[Seed], [AsciiCodeLowerCaseLetterInner], [AsciiCodeLowerCaseLetterOuter]], ComplexArgs),
        
        ComplexInner =.. [ComplexNameInner|ComplexArgs],
        Complex =.. [ComplexNameOuter|[ComplexInner]].

% Generate Atoms
ranatom(Seed, Atom):-
        % Reset random
        setrand(Seed),

        random(97, 123, AsciiCodeLowerCaseLetter_1),
        random(97, 123, AsciiCodeLowerCaseLetter_2),

        atom_codes(myatom_, PrefixCodes),
        number_codes(Seed, SeedCodes),
        append([PrefixCodes, [AsciiCodeLowerCaseLetter_1], [AsciiCodeLowerCaseLetter_2], SeedCodes], AtomCodes),
        atom_codes(Atom, AtomCodes).
        
/*************
 * Benchmark *
 *************/
% The order of the headlines is important.
% They appear in the csv file in the order in wich they are listed here.
csv_headlines(bench_insert, ['emptyloop',
                             'garbage_collection_init', 'garbage_collection_insert', 'garbage_collector_calls_init', 'garbage_collector_calls_insert',
                             'init_insert', 'insert', 'runtime_init_insert', 'runtime_insert',
                             'global_stack_init', 'global_stack_insert', 'heap_init', 'heap_insert']).
csv_headlines(bench_insert_operation_count_variation, CSVHeadlines):- csv_headlines(bench_insert, CSVHeadlines).
csv_headlines(bench_insert_data_structure_size_variation, CSVHeadlines):- csv_headlines(bench_insert, CSVHeadlines).

csv_headlines(bench_access, ['emptyloop',
                             'garbage_collection_hit', 'garbage_collection_miss', 'garbage_collector_calls_init', 'garbage_collector_calls_hit', 'garbage_collector_calls_miss',
                             'access', 'access_miss', 'runtime_access', 'runtime_access_miss',
                             'global_stack_init', 'global_stack_access', 'global_stack_miss', 'heap_init', 'heap_access', 'heap_miss']).
csv_headlines(bench_access_operation_count_variation, CSVHeadlines):- csv_headlines(bench_access, CSVHeadlines).
csv_headlines(bench_access_miss_chance_variation, CSVHeadlines):- csv_headlines(bench_access, CSVHeadlines).
csv_headlines(bench_access_data_structure_size_variation, CSVHeadlines):- csv_headlines(bench_access, CSVHeadlines).
csv_headlines(bench_access_without_lists, CSVHeadlines):- csv_headlines(bench_access, CSVHeadlines).


bench(BenchPred, DataStructureName, DataPatternName, AdditionalArgs, StepsPred, StepsArgs, RepeatsPerPattern, FileDirectory, FileNameAddon):-
        % DataSet sizes.
        StepsCall =.. ([StepsPred|[Steps|StepsArgs]]),
        call(StepsCall),
        
        % Build file name and directory.
        build_directory(FileDirectory),
        build_filename(FileDirectory, [DataStructureName|[BenchPred|[DataPatternName|[StepsPred]]]], FileNameAddon, FileName),
        
        % Runtime info
        format('Start with ~s ...~n', [FileName]),

        % Run benchmarks.
        findall(X,
                (
                    % Select N
                    member(N, Steps),
                    % Build bench pred.
                    append([[DataStructureName], [DataPatternName], AdditionalArgs, [N, RepeatsPerPattern, X]], Args),
                    BenchCall =.. [BenchPred|Args],
                    call(BenchCall)
                ), Results),

        % CSV headlines
        csv_headlines(BenchPred, CSVHeadlines),
        
        % Write output as .csv file
        write_results(FileName, Results, CSVHeadlines),

        % Runtime info
        format('Finished with ~s!~n~n', [FileName]).

/********************
 * Benchmark Insert *
 ********************/        
bench_insert(DataStructureName, DataPatternName, DataStructureSize, GarbageCollection, OpCount, Repeats, R):-
        % Select Predicates
        data_structure(DataStructureName, InitPred, InsertPred, _, DeletePred, ClearPred), !,
                      
        % Generate test pattern
        data_pattern(DataPatternName, DataSetPred, PatternHit, _),
        
        (DataStructureSize is 0 ->
                DataSet = [],
                InsertPattern = []
        ;
                call(DataSetPred, DataSet, DataStructureSize),
                call(PatternHit, InsertPattern, DataSet, OpCount)
        ),

        
        % Runtime info
        format('~w: Start bench_insert, data structure size ~d, gc ~w, operation count ~d ...~n', [DataStructureName, DataStructureSize, GarbageCollection, OpCount]),

        % Enable/Disable Garbage Collection
        set_prolog_flag(gc, GarbageCollection),

        % Generate benchmarks
        findall([TEmpty,
                 TGarbageCollectionInit, TGarbageCollectionInsert, GarbageCollectorCallsInit, GarbageCollectorCallsInsert,
                 TInit, TInsert, TRInit, TRInsert,
                 MemGlobalStackInit, MemGlobalStack, MemHeapInit, MemHeap],
                (
                    steps(1, Repeats, 1, X),
                    
                    % Empty loop
                    statistics(walltime, [TEmpty0|_]),
                    empty_loop(DataSet),
                    statistics(walltime, [TEmpty1|_]),
                    TEmpty is TEmpty1 - TEmpty0,

                    % Init data structure
                    call(InitPred, EmptyDataStructure, DataStructureSize),

                    % Insert initial elements
                    % Runtime
                    statistics(walltime, [TInit0|_]),
                    statistics(runtime, [TRInit0|_]),             
                    statistics(garbage_collection, [GarbageCollectorCallsInit0, _, TGarbageCollectionInit0]),       
                    % Memory                 
                    statistics(global_stack, [MemGlobalStackInit0|_]),
                    statistics(heap, [MemHeapInit0|_]),

                    (call(InsertPred, DataSet, EmptyDataStructure, DataStructure) -> true ; write('### Initial Insert Failed! ###\n')),

                    % Runtime
                    statistics(walltime, [TInit1|_]),
                    statistics(runtime, [TRInit1|_]),       
                    statistics(garbage_collection, [GarbageCollectorCallsInit1, _, TGarbageCollectionInit1]),            
                    % Memory               
                    statistics(global_stack, [MemGlobalStackInit1|_]),
                    statistics(heap, [MemHeapInit1|_]),
                    
                    TInit is TInit1 - TInit0,
                    TRInit is TRInit1 - TRInit0,
                    TGarbageCollectionInit is TGarbageCollectionInit1 - TGarbageCollectionInit0,
                    GarbageCollectorCallsInit is GarbageCollectorCallsInit1 - GarbageCollectorCallsInit0,
                    MemGlobalStackInit is MemGlobalStackInit1 - MemGlobalStackInit0,
                    MemHeapInit is MemHeapInit1 - MemHeapInit0,
                     
                    % Insert
                    % Runtime
                    statistics(walltime, [TInsert0|_]),
                    statistics(runtime, [TRInsert0|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsInsert0, _, TGarbageCollectionInsert0]),

                    % Memory           
                    statistics(global_stack, [MemGlobalStack0|_]),
                    statistics(heap, [MemHeap0|_]),
                    
                    (call(InsertPred, InsertPattern, DataStructure, _) -> true ; write('### Insert Failed! ###\n')),

                    % Runtime
                    statistics(walltime, [TInsert1|_]),
                    statistics(runtime, [TRInsert1|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsInsert1, _, TGarbageCollectionInsert1]),

                    % Memory             
                    statistics(global_stack, [MemGlobalStack1|_]),
                    statistics(heap, [MemHeap1|_]),
                    
                    TInsert is TInsert1 - TInsert0,
                    TRInsert is TRInsert1 - TRInsert0,
                    TGarbageCollectionInsert is TGarbageCollectionInsert1 - TGarbageCollectionInsert0,
                    GarbageCollectorCallsInsert is GarbageCollectorCallsInsert1 - GarbageCollectorCallsInsert0,

                    MemGlobalStack is MemGlobalStack1 - MemGlobalStack0,
                    MemHeap is MemHeap1 - MemHeap0,
                    
                    % Runtime info
                    format('~d/~d: WalltimeInit:~d, WalltimeInsert:~d, RuntimeInit:~d, RuntimeInsert:~d.\n',
                           [X, Repeats, TInit, TInsert, TRInit, TRInsert]),
                    format('\tMemoryGlobalStackInit:~d, MemoryGlobalStack:~d, MempoyHeapInit:~d, MemoryHeap:~d.\n',
                           [MemGlobalStackInit, MemGlobalStack, MemHeapInit, MemHeap]),
                    format('\tGarbageCollectorInit:~d, GarbageCollectorInsert:~d, GarbageCollectionCallsInit:~d, GarbageCollectionCallsInsert:~d.\n',
                           [TGarbageCollectionInit, TGarbageCollectionInsert, GarbageCollectorCallsInit, GarbageCollectorCallsInsert]),                    

                    % Clear/Delete elements
                    ((DataStructureName = blackboard) -> call(DeletePred, DataSet, DataStructure, _) ; call(ClearPred, DataStructure, _))
                ), R),

        % Enable Garbage Collection
        set_prolog_flag(gc, on),
        
        % Runtime info
        write('done.\n').

bench_insert_operation_count_variation(DataStructureName, DataPatternName, DataStructureSize, GarbageCollection, OpCount, Repeats, [OpCount|R]):-
        % Generate benchmarks
        bench_insert(DataStructureName, DataPatternName, DataStructureSize, GarbageCollection, OpCount, Repeats, R).
        
bench_insert_data_structure_size_variation(DataStructureName, DataPatternName, OpCount, GarbageCollection, DataStructureSize, Repeats, [DataStructureSize|R]):-
        % Generate benchmarks
        bench_insert(DataStructureName, DataPatternName, DataStructureSize, GarbageCollection, OpCount, Repeats, R).
       
/********************
 * Benchmark Access *
 ********************/
bench_access(DataStructureName, DataPatternName, DataStructureSize, MissPercentage, GarbageCollection, OpCount, Repeats, R):-
        % Runtime info
        format('~w: Start bench_access, data structure size ~d, gc ~w, operation count ~d ...\n', [DataStructureName, DataStructureSize, GarbageCollection, OpCount]),

        % Select Predicates
        data_structure(DataStructureName, InitPred, InsertPred, AccessPred, DeletePred, ClearPred), !,

        % Generate test patterns
        data_pattern(DataPatternName, DataSetPred, AccessPatternPred, MissPatternPred), !,
        AccessCountHit is (OpCount * (100 - MissPercentage)) div 100,
        AccessCountMiss is (OpCount * MissPercentage) div 100,
        
        (DataStructureSize is 0 ->
                DataSet = [],
                AccessPatternHit = [],
                AccessPatternMiss = []
        ;
                call(DataSetPred, DataSet, DataStructureSize),
                call(AccessPatternPred, AccessPatternHit, DataSet, AccessCountHit),
                call(MissPatternPred, AccessPatternMiss, DataSet, AccessCountMiss)
        ),

        % Runtime info
        format('MissPercentage:~2f, Hit:~d, Miss:~d\n', [MissPercentage, AccessCountHit, AccessCountMiss]),

        % Enable/Disable Garbage Collection
        set_prolog_flag(gc, GarbageCollection),
        
        findall([TEmpty,
                 TGarbageCollectionHit, TGarbageCollectionMiss, GarbageCollectorCallsInit, GarbageCollectorCallsHit, GarbageCollectorCallsMiss,
                 TAccessHit, TAccessMiss, TRAccessHit, TRAccessMiss,
                 MemGlobalStackInit, MemGlobalStackHit, MemGlobalStackMiss, MemHeapInit, MemHeapHit, MemHeapMiss],
                (
                    steps(1, Repeats, 1, X),

                    % Memory Init        
                    statistics(garbage_collection, [GarbageCollectorCallsInit0, _, _]),
                    statistics(global_stack, [MemGlobalStackInit0|_]),
                    statistics(heap, [MemHeapInit0|_]),

                    % Init data structure
                    call(InitPred, EmptyDataStructure, DataStructureSize),
                    call(InsertPred, DataSet, EmptyDataStructure, DataStructure),

                    % Memory Init            
                    statistics(garbage_collection, [GarbageCollectorCallsInit1, _, _]),
                    statistics(global_stack, [MemGlobalStackInit1|_]),
                    statistics(heap, [MemHeapInit1|_]),

                    MemGlobalStackInit is MemGlobalStackInit1 - MemGlobalStackInit0,
                    MemHeapInit is MemHeapInit1 - MemHeapInit0,
                    GarbageCollectorCallsInit is GarbageCollectorCallsInit1 - GarbageCollectorCallsInit0,

                    % Empty loop
                    statistics(walltime, [TEmpty0|_]),
                    empty_loop(AccessPatternHit),
                    empty_loop(AccessPatternMiss),
                    statistics(walltime, [TEmpty1|_]),
                    TEmpty is TEmpty1 - TEmpty0,
               
                    % Access Hit
                    % Runtime Hit
                    statistics(walltime, [TAccessHit0|_]),
                    statistics(runtime, [TRAccessHit0|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsHit0, _, TGarbageCollectionHit0]),
                    % Memory Hit             
                    statistics(global_stack, [MemGlobalStackHit0|_]),
                    statistics(heap, [MemHeapHit0|_]),
                    
                    (call(AccessPred, AccessPatternHit, DataStructure) -> true ; write('### Access Hit Failed ###\n')),

                    %Runtime Hit
                    statistics(walltime, [TAccessHit1|_]),
                    statistics(runtime, [TRAccessHit1|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsHit1, _, TGarbageCollectionHit1]),
                    %Memory Hit
                    statistics(global_stack, [MemGlobalStackHit1|_]),
                    statistics(heap, [MemHeapHit1|_]),
                    
                    TAccessHit is TAccessHit1 - TAccessHit0,
                    TRAccessHit is TRAccessHit1 - TRAccessHit0,
                    TGarbageCollectionHit is TGarbageCollectionHit1 - TGarbageCollectionHit0,
                    MemGlobalStackHit is MemGlobalStackHit1 - MemGlobalStackHit0,
                    MemHeapHit is MemHeapHit1 - MemHeapHit0,
                    GarbageCollectorCallsHit is GarbageCollectorCallsHit1 - GarbageCollectorCallsHit0,

                    % Access Miss
                    % Runtime Miss
                    statistics(walltime, [TAccessMiss0|_]),
                    statistics(runtime, [TRAccessMiss0|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsMiss0, _, TGarbageCollectionMiss0]),
                    % Memory Miss
                    statistics(global_stack, [MemGlobalStackMiss0|_]),
                    statistics(heap, [MemHeapMiss0|_]),

                    (call(AccessPred, AccessPatternMiss, DataStructure) -> true ; write('### Access Miss Failed ###\n')),

                    % Runtime Miss
                    statistics(walltime, [TAccessMiss1|_]),
                    statistics(runtime, [TRAccessMiss1|_]),
                    statistics(garbage_collection, [GarbageCollectorCallsMiss1, _, TGarbageCollectionMiss1]),
                    % Memory Miss
                    statistics(global_stack, [MemGlobalStackMiss1|_]),
                    statistics(heap, [MemHeapMiss1|_]),
                    
                    TAccessMiss is TAccessMiss1 - TAccessMiss0,
                    TRAccessMiss is TRAccessMiss1 - TRAccessMiss0,
                    TGarbageCollectionMiss is TGarbageCollectionMiss1 - TGarbageCollectionMiss0,
                    MemGlobalStackMiss is MemGlobalStackMiss1 - MemGlobalStackMiss0,
                    MemHeapMiss is MemHeapMiss1 - MemHeapMiss0,
                    GarbageCollectorCallsMiss is GarbageCollectorCallsMiss1 - GarbageCollectorCallsMiss0,

                    % Runtime info
                    format('~d/~d: WalltimeHit:~d, WalltimeMiss:~d, RuntimeHit:~d, RuntimeMiss:~d, GarbageCollectionHit:~d, GarbageCollectionMiss:~d.\n',
                           [X, Repeats, TAccessHit, TAccessMiss, TRAccessHit, TRAccessMiss, TGarbageCollectionHit, TGarbageCollectionMiss]),
                    format('\tMemoryGlobalStackInit:~d, MemoryGlobalStackHit:~d, MemoryGlobalStackMiss:~d, MemoryHeapInit:~d, MemoryHeapHit:~d, MemoryHeapMiss:~d.\n',
                           [MemGlobalStackInit, MemGlobalStackHit, MemGlobalStackMiss, MemHeapInit, MemHeapHit, MemHeapMiss]),
                    format('\tTimeGarbageCollectorInit:~d, TimeGarbageCollectorInsert:~d, GarbageCollectionCallsInit:~d, GarbageCollectionCallsHit:~d, GarbageCollectionCallsMiss:~d.\n',
                           [TGarbageCollectionHit, TGarbageCollectionMiss, GarbageCollectorCallsInit, GarbageCollectorCallsHit, GarbageCollectorCallsMiss]),
                    
                    % Clear/Delete elements
                    ((DataStructureName = blackboard) -> call(DeletePred, DataSet, DataStructure, _) ; call(ClearPred, DataStructure, _))
                ), R),

        % Enable Garbage Collection
        set_prolog_flag(gc, on),

        % Runtime info
        write('done.\n').
                 
bench_access_operation_count_variation(DataStructureName, DataPatternName, DataStructureSize, MissPercentage, GarbageCollection, OpCount, Repeats, [OpCount|R]):-
        % Generate benchmarks
        bench_access(DataStructureName, DataPatternName, DataStructureSize, MissPercentage, GarbageCollection, OpCount, Repeats, R).

bench_access_miss_chance_variation(DataStructureName, DataPatternName, DataStructureSize, OpCount, GarbageCollection, MissPercentage, Repeats, [MissPercentage|R]):-
        % Generate benchmarks
        bench_access(DataStructureName, DataPatternName, DataStructureSize, MissPercentage, GarbageCollection, OpCount, Repeats, R).

bench_access_data_structure_size_variation(DataStructureName, DataPatternName, OpCount, MissPercentage, GarbageCollection, DataStructureSize, Repeats, [DataStructureSize|R]):-
        % Generate benchmarks
        bench_access(DataStructureName, DataPatternName, DataStructureSize, MissPercentage, GarbageCollection, OpCount, Repeats, R).


/********************
 * Benchmark Delete *
 ********************/   
bench_delete(DataStructureName, DataPatternName, N, M, [N|R]):-
        % Select Predicates
        data_structure(DataStructureName, InitPred, InsertPred, _, DeletePred, _), !,
        
        % Generate test pattern
        data_pattern(DataPatternName, DataSetPred, _, _),
        call(DataSetPred, DataSet, N),

        % Runtime info
        format('~w: Start bench_delete, dataset size ~d ... ', [DataStructureName, N]),
        
        % Generate benchmarks
        findall([TEmpty, TDelete],
                (
                    steps(1, M, 1, _),

                    % Init data structure
                    call(InitPred, EmptyDataStructure, N),
                    call(InsertPred, DataSet, EmptyDataStructure, DataStructure),
                    
                    % Empty loop
                    statistics(walltime, [TEmpty0|_]),
                    empty_loop10(DataSet),
                    statistics(walltime, [TEmpty1|_]),
                    TEmpty is TEmpty1 - TEmpty0,
                            
                    % Delete
                    statistics(walltime, [TDelete0|_]),
                    call(DeletePred, DataSet, DataStructure, _),
                    statistics(walltime, [TDelete1|_]),
                    TDelete is TDelete1 - TDelete0
                ), R),
        
        % Runtime info
        write('done.\n').
                        
/**********
 * Output *   
 **********/
% Output is generated as a csv file.
% Each line contains the data for a sample size.
% The csv file looks something like this:
% Sample Size , Headlines_1, Headlines_2, ... 
%  N1, Value1, Value2, ...
%  N2, Value1, Value2, ...
% ...,    ...,    ..., ...
write_results(FileName, Results, Headlines):-
        Results = [[_|T]|_],
        length(T, N),
        open(FileName, write, InStream),
        write_table_headline(InStream, N, Headlines),
        write_lines(InStream, Results),
        close(InStream).

write_table_headline(InStream, N, Headlines):-
        format(InStream, '~s', ['Sample Size']),
        findall(_,
                (
                    steps(1, N, 1, K),
                    write_headlines(InStream, Headlines, K)
                ), _),
        write(InStream, '\n').

write_lines(InStream, Results):-
        findall(_,
                (
                    member([N|Data], Results),
                    format(InStream, '~2f', [N]),
                    write_line(InStream, Data),
                    write(InStream, '\n')
                ), _).

write_line(InStream, Data):-
        findall(_,
                (
                    member(X, Data),
                    write_list_int(InStream, X)
                ), _).

write_headlines(_, [], _).
write_headlines(InStream, [H|T], N):-
        format(InStream, ',~s_~d', [H, N]),
        write_headlines(InStream, T, N).

write_list_int(_, []).
write_list_int(InStream, [H|T]):-
        format(InStream, ',~3d', [H]),
        write_list_int(InStream, T).

/*****************
 * Data Patterns * 
 *****************/
% Data Pattern Complex Terms
% Complex terms are of shape 'term_[a-z](term_[a-z](number, number, number))'
data_pattern(rancomplex, dataset_rancomplexterms, pattern_rancomplex, misspattern_complex).

% Data Pattern 1, ..., N-1, N
% Access Pattern random element from (1, ..., N-1, N)
% Miss Pattern random element from (-1, N+1)
data_pattern(rannumbers, dataset_intran, pattern_ranint, misspattern_int).

% Data Pattern 10, 20, ..., (N-1)*10, N*10
% Access Pattern random element from (10, ..., (N-1)*10, N*10)
% Miss pattern random numbers x, so that x mod 10 =/= 0 and 0 < x < N*10
data_pattern(rannumbers10, dataset_intran10, pattern_ranint10, misspattern_int10).

% Data Pattern Atoms
% Atoms are of shape 'myatom_[a-z][a-z][number]'
data_pattern(ranatoms, dataset_atoms, pattern_atoms, misspattern_atoms).

/************
 * Datasets *
 ************/
%%%%% List of ones %%%%%
dataset_intones([], 0).
dataset_intones([1|T], N):-
        N > 0, !,
        M is N - 1,
        dataset_intones(T, M).
        
%%%%% List of increasing integer numbers %%%%%
dataset_intinc(L, N):-
        dataset_intinc(L, 1, N).
dataset_intinc([N], N, N):- !.
dataset_intinc([M|T], M, N):-
        M =< N, !,
        NewM is M + 1, 
        dataset_intinc(T, NewM, N).

%%%%% List of decreasing integer numbers %%%%%
dataset_intdec([], 0):- !.
dataset_intdec([N|T], N):-
        N > 0, !,
        M is N-1,
        dataset_intdec(T, M). 

%%%%% Permutation of list of numbers from 1 to N %%%%%
dataset_intran(L, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        % Generate int list to randomize
        dataset_intinc(IntegerList, N),

        % Permute elements
        random_permutation(IntegerList, L).

%%%%% Permutation of list of numbers from 10 to N*10 in steps of 10 %%%%%
dataset_intran10(L, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        UpperBound is N * 10,
        
        % Generate int list to randomize
        findall(X, steps(10, UpperBound, 10, X), R),
        
        % Permute elements
        random_permutation(R, L).        

%%%%% List of random complex terms %%%%%
dataset_rancomplexterms(L, N):-
        % Generate random complex terms
        findall([ComplexTerm],
                (
                    steps(1, N, 1, Seed),
                    rancomplexterm(Seed, ComplexTerm)
                ), R),
        
        % Flatten list
        append(R, L).

%%%%% List of random atoms %%%%%
dataset_atoms(L, N):-
        % Generate random complex terms
        findall([Atom],
                (
                    steps(1, N, 1, Seed),
                    ranatom(Seed, Atom)
                ), R),
        
        % Flatten list
        append(R, L).   

/**************************
 * Access/Insert Patterns *
 **************************/
% Goal is to avoid long random selection times of random_member

%%%%% Random Integer Numbers for dataset_intran %%%%%
% Only works for DataSets with Pattern (1, 2, ..., M-1, M)!
pattern_ranint(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        UpperBound is Length + 1,
        
        % Generate random integer numbers
        findall([Element],
                (
                    steps(1, N, 1, _),
                    random(1, UpperBound, Element)
                ), R),
        
        % Flatten list
        append(R, Pattern).

%%%%% Random Integer Numbers for dataset_intran10 %%%%%
% Only works if dataset is generated with dataset_intran10!
pattern_ranint10(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        UpperBound is Length + 1,
        
        % Generate random integer numbers
        findall([Element],
                (
                    steps(1, N, 1, _),
                    random(1, UpperBound, RandomNumber),
                    Element is RandomNumber * 10
                ), R),
        
        % Flatten list
        append(R, Pattern).

%%%%% Random Complex %%%%%
% Only works if dataset is generated with dataset_rancomplexterms!
pattern_rancomplex(AccessPattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        UpperBound is Length + 1,

        % Generate random complex terms
        findall([Term],
                (
                    steps(1, N, 1, _),
                    random(1, UpperBound, TermSeed),
                    rancomplexterm(TermSeed, Term)
                ), R),

        % Flatten list
        append(R, AccessPattern).

%%%%% Random Atom %%%%%
pattern_atoms(AccessPattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        UpperBound is Length + 1,

        % Generate random atoms
        findall([Atom],
                (
                    steps(1, N, 1, _),
                    random(1, UpperBound, AtomSeed),
                    ranatom(AtomSeed, Atom)
                ), R),

        % Flatten list
        append(R, AccessPattern).
        
/*****************
 * Miss Patterns *
 *****************/
%%%%% Miss Pattern Integer for dataset_intran %%%%%
% Only works on datasets of type 1, 2, ..., N
% Selects random int X = -1 or X = N+1
misspattern_int(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),
        
        length(DataSet, Length),
        LowValue is -1,
        HighValue is Length + 1, 
        
        findall([Element],
                (
                    steps(1, N, 1, _),
                    random(0, 2, ValueSelection),
                    (ValueSelection is 0 -> Element is LowValue ; Element is HighValue)
                ), R),

        % Flatten list
        append(R, Pattern).

%%%%% Miss Pattern Integer for dataset_intran10 %%%%%
% Only works on datasets of type 10, 20, ..., length(Dataset)*10
misspattern_int10(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),
        
        length(DataSet, Length),
        UpperBound is Length + 2,
        
        findall([Element],
                (
                    steps(1, N, 1, _),
                    random(1, UpperBound, RandomNumber),
                    random(1, 10, RandomNumberDiff),
                    Element is (RandomNumber * 10) - RandomNumberDiff                 
                ), R),

        % Flatten list
        append(R, Pattern).

%%%%% Miss Pattern Complex %%%%%
% Only works if dataset is generated with dataset_rancomplexterms!
misspattern_complex(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        LowerBound is Length + 1,
        UpperBound is LowerBound * 2,

        % Generate random complex terms
        findall([Term],
                (
                    steps(1, N, 1, _),
                    random(LowerBound, UpperBound, TermSeed),
                    rancomplexterm(TermSeed, Term)
                ), R),

        % Flatten list
        append(R, Pattern).

%%%%% Miss Pattern Atoms %%%%%
misspattern_atoms(Pattern, DataSet, N):-
        % Reset random
        randomseed(Seed), !,
        setrand(Seed),

        length(DataSet, Length),
        LowerBound is Length + 1,
        UpperBound is LowerBound * 2,

        % Generate random atoms
        findall([Atom],
                (
                    steps(1, N, 1, _),
                    random(LowerBound, UpperBound, TermSeed),
                    ranatom(TermSeed, Atom)
                ), R),

        % Flatten list
        append(R, Pattern).

/*****************
 * Step Patterns *
 *****************/
%%%%% Linear %%%%%
steps_linear(Steps, LowerBound, UpperBound, StepSize):-
        findall(Step, steps(LowerBound, UpperBound, StepSize, Step), Steps).    

/*******************
 * Data structures *
 *******************/
%%%%% Definition of datastructures %%%%%
data_structure(avl, anew, ainsert, aaccess, adelete, aclear).
data_structure(avl_fchk, anew, a_with_fetch_check_insert, aaccess, adelete, aclear).
data_structure(orderedset, osetnew, osetinsert, osetaccess, osetdelete, osetclear).
data_structure(orderedset10, osetnew, osetinsert10, osetaccess10, osetdelete10, osetclear).
data_structure(orderedset100, osetnew, osetinsert100, osetaccess100, osetdelete100, osetclear).
data_structure(orderedsettuple, osetnew, osetinsert_tuple, osetaccess_tuple, osetdelete_tuple, osetclear_tuple).
data_structure(list, lnew, linsert, laccess, ldelete, lclear).
data_structure(list_without_duplicates, lnew, linsert_no_duplicates, laccess, ldelete, lclear).
data_structure(mutarray, manew, mainsert, maaccess, madelete, maclear).
data_structure(mutdict, mnew, minsert, maccess, mdelete, mclear).
data_structure(blackboard, bnew, binsert, baccess, bdelete, bclear).
data_structure(assertds, assertnew, assertinsert, assertaccess, assertdelete, assertclear).

%%%%% AVL %%%%%
% init
anew(AVL, _):-
        empty_avl(AVL).

% insert
ainsert([],A,A).
ainsert([H|T],In,Out) :-
        avl_store(H,In,true,In2),
        ainsert(T,In2,Out).

% access
aaccess([], _).
aaccess([H|T], Avl):-
        (avl_fetch(H, Avl, _) -> true ; true),
        aaccess(T, Avl).

% delete
adelete([], Out, Out).
adelete([H|T], In, Out):-
        avl_delete(H, In, true, In2),
        adelete(T, In2, Out).

% clear
aclear(AVL, AVLClear):-
        avl_to_list(AVL, KeyValueList),
        findall(Key, member(Key-_, KeyValueList), R),
        adelete(R, AVL, AVLClear).
        
%%%%% Avl With Fetch Check %%%%%
% insert
a_with_fetch_check_insert([],A,A).
a_with_fetch_check_insert([H|T],In,Out) :-
        (avl_fetch(H,In,true) -> In2=In % first check if it is already in the tree; avoid copying the term
        ; avl_store(H,In,true,In2)),
        a_with_fetch_check_insert(T,In2,Out).

%%%%% list %%%%%
% init
lnew([], _).

% insert
linsert([], Out, Out).
linsert([H|T], In, Out):-
        linsert(T, [H|In], Out).

% access
laccess([], _).
laccess([H|T], L):-
        (memberchk(H, L) -> true ; true),
        laccess(T, L).

% delete
ldelete([], A, A).
ldelete([H|T], In, Out):-
        delete(In, H, In2),
        ldelete(T, In2, Out).

% clear
lclear(L, LClear):-
        ldelete(L, L, LClear).

%%%%% list without duplicates %%%%%

% insert
linsert_no_duplicates([], Out, Out).
linsert_no_duplicates([H|T], In, Out):-
       memberchk(H, In) -> linsert_no_duplicates(T, In, Out)
       ; linsert_no_duplicates(T, [H|In], Out).

%%%%% mutarray %%%%%
% init
manew(Mutarray, N):-
        new_mutarray(Mutarray, N).

% insert
mainsert([],A,A).
mainsert([H|T],In,Out):-
        mutarray_put(In, H, true),
        mainsert(T, In, Out).

% access
maaccess([], _).
maaccess([H|T], MutArray):-
        (mutarray_get(MutArray, H, _) -> true ; true),
        maaccess(T, MutArray).        

% delete
madelete([], A, A).
madelete([H|T], In, Out):-
        mutarray_put(In, H, empty),
        madelete(T, In, Out).

% clear
maclear(Mutarray, MutarrayClear):-
        mutarray_length(Mutarray, Length),
        findall(X, steps(1, Length, 1, X), R),
        madelete(R, Mutarray, MutarrayClear).

%%%%% mutdict %%%%%
% init
mnew(Mutdict, _):-
        new_mutdict(Mutdict).

% insert
minsert([], A, A).
minsert([H|T], In, Out):-
        mutdict_put(In, H, true),
        minsert(T, In, Out).

% access
maccess([], _).
maccess([H|T], MutDict):-
        (mutdict_get(MutDict, H, _) -> true ; true),
        maccess(T, MutDict).

% delete
mdelete([], A, A).
mdelete([H|T], In, Out):-
   mutdict_delete(In, H),
   mdelete(T, In, Out).

% clear
mclear(MutDict, MutDict):-
        mutdict_clear(MutDict).

%%%%% blackboard %%%%%
% init
bnew(_, _).

% insert
binsert([], _, _).
binsert([H|T], _, _):- 
        bb_put(H, true),
        binsert(T, _, _).              

% access
baccess([], _).
baccess([H|T], _):-
        (bb_get(H, _) -> true ; true),
        baccess(T, _).

% delete
bdelete([], _, _).
bdelete([H|T], _, _):-
        bb_delete(H, _),
        bdelete(T, _, _).

% clear
bclear(_, _).

%%%%% Assert/Lookup %%%%%
:- dynamic mydb/2.

% init
assertnew(_, _).

% insert
assertinsert([], _, _).
assertinsert([H|T], _, _):-
        assert(mydb(H, true)),
        assertinsert(T, _, _).

% access
assertaccess([], _).
assertaccess([H|T], _):-
        (mydb(H, _) -> true ; true),
        assertaccess(T, _).

% delete
assertdelete([], _, _).
assertdelete([H|T], _, _):-
        retract(mydb(H, _)),
        assertdelete(T, _, _).

% clear
assertclear(_, _):-
        retractall(mydb(_, _)).

%%%%% Ordered Set Tuple %%%%%
% insert
osetinsert_tuple([], Out, Out).
osetinsert_tuple([H|T], In, Out):-
        ord_add_element(In, tuple(H, true), In2),
        osetinsert_tuple(T, In2, Out).

% access
osetaccess_tuple([],_).
osetaccess_tuple([H|T], OSet):-
        (ord_member(tuple(H,_), OSet) -> true ; true),
        osetaccess_tuple(T, OSet).

% delete
osetdelete_tuple([], Out, Out).
osetdelete_tuple([H|T], In, Out):-
        ord_del_element(In, tuple(H,_), In2),
        osetdelete_tuple(T, In2, Out).


% clear
osetclear_tuple(OrderedSet, OrderedSetClear):-
        osetdelete_tuple(OrderedSet, OrderedSet, OrderedSetClear).


%%%%% Ordered Set %%%%%
% init
osetnew([], _).

% insert list
osetinsert([], Out, Out).
osetinsert([H|T], In, Out):-
        ord_add_element(In, H, In2),
        osetinsert(T, In2, Out).

% insert 10
osetinsert10([], Out, Out).
osetinsert10([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10|T], In, Out):-
        ord_add_element(In, E1, In0),
        ord_add_element(In0, E2, In1),
        ord_add_element(In1, E3, In2),
        ord_add_element(In2, E4, In3),
        ord_add_element(In3, E5, In4),
        ord_add_element(In4, E6, In5),
        ord_add_element(In5, E7, In6),
        ord_add_element(In6, E8, In7),
        ord_add_element(In7, E9, In8),
        ord_add_element(In8, E10, In9),
        osetinsert10(T, In9, Out).

% insert 100
osetinsert100([], Out, Out).
osetinsert100([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10,
               E11, E12, E13, E14, E15, E16, E17, E18, E19, E20,
               E21, E22, E23, E24, E25, E26, E27, E28, E29, E30,
               E31, E32, E33, E34, E35, E36, E37, E38, E39, E40,
               E41, E42, E43, E44, E45, E46, E47, E48, E49, E50,
               E51, E52, E53, E54, E55, E56, E57, E58, E59, E60,
               E61, E62, E63, E64, E65, E66, E67, E68, E69, E70,
               E71, E72, E73, E74, E75, E76, E77, E78, E79, E80,
               E81, E82, E83, E84, E85, E86, E87, E88, E89, E90,
               E91, E92, E93, E94, E95, E96, E97, E98, E99, E100|T], In, Out):-
        ord_add_element(In, E1, In0),
        ord_add_element(In0, E2, In1),
        ord_add_element(In1, E3, In2),
        ord_add_element(In2, E4, In3),
        ord_add_element(In3, E5, In4),
        ord_add_element(In4, E6, In5),
        ord_add_element(In5, E7, In6),
        ord_add_element(In6, E8, In7),
        ord_add_element(In7, E9, In8),
        ord_add_element(In8, E10, In9),
        
        ord_add_element(In9, E11, In10),
        ord_add_element(In10, E12, In11),
        ord_add_element(In11, E13, In12),
        ord_add_element(In12, E14, In13),
        ord_add_element(In13, E15, In14),
        ord_add_element(In14, E16, In15),
        ord_add_element(In15, E17, In16),
        ord_add_element(In16, E18, In17),
        ord_add_element(In17, E19, In18),
        ord_add_element(In18, E20, In19),
        
        ord_add_element(In19, E21, In20),
        ord_add_element(In20, E22, In21),
        ord_add_element(In21, E23, In22),
        ord_add_element(In22, E24, In23),
        ord_add_element(In23, E25, In24),
        ord_add_element(In24, E26, In25),
        ord_add_element(In25, E27, In26),
        ord_add_element(In26, E28, In27),
        ord_add_element(In27, E29, In28),
        ord_add_element(In28, E30, In29),
        
        ord_add_element(In29, E31, In30),
        ord_add_element(In30, E32, In31),
        ord_add_element(In31, E33, In32),
        ord_add_element(In32, E34, In33),
        ord_add_element(In33, E35, In34),
        ord_add_element(In34, E36, In35),
        ord_add_element(In35, E37, In36),
        ord_add_element(In36, E38, In37),
        ord_add_element(In37, E39, In38),
        ord_add_element(In38, E40, In39),
        
        ord_add_element(In39, E41, In40),
        ord_add_element(In40, E42, In41),
        ord_add_element(In41, E43, In42),
        ord_add_element(In42, E44, In43),
        ord_add_element(In43, E45, In44),
        ord_add_element(In44, E46, In45),
        ord_add_element(In45, E47, In46),
        ord_add_element(In46, E48, In47),
        ord_add_element(In47, E49, In48),
        ord_add_element(In48, E50, In49),

        ord_add_element(In49, E51, In50),
        ord_add_element(In50, E52, In51),
        ord_add_element(In51, E53, In52),
        ord_add_element(In52, E54, In53),
        ord_add_element(In53, E55, In54),
        ord_add_element(In54, E56, In55),
        ord_add_element(In55, E57, In56),
        ord_add_element(In56, E58, In57),
        ord_add_element(In57, E59, In58),
        ord_add_element(In58, E60, In59),
        
        ord_add_element(In59, E61, In60),
        ord_add_element(In60, E62, In61),
        ord_add_element(In61, E63, In62),
        ord_add_element(In62, E64, In63),
        ord_add_element(In63, E65, In64),
        ord_add_element(In64, E66, In65),
        ord_add_element(In65, E67, In66),
        ord_add_element(In66, E68, In67),
        ord_add_element(In67, E69, In68),
        ord_add_element(In68, E70, In69),
        
        ord_add_element(In69, E71, In70),
        ord_add_element(In70, E72, In71),
        ord_add_element(In71, E73, In72),
        ord_add_element(In72, E74, In73),
        ord_add_element(In73, E75, In74),
        ord_add_element(In74, E76, In75),
        ord_add_element(In75, E77, In76),
        ord_add_element(In76, E78, In77),
        ord_add_element(In77, E79, In78),
        ord_add_element(In78, E80, In79),
        
        ord_add_element(In79, E81, In80),
        ord_add_element(In80, E82, In81),
        ord_add_element(In81, E83, In82),
        ord_add_element(In82, E84, In83),
        ord_add_element(In83, E85, In84),
        ord_add_element(In84, E86, In85),
        ord_add_element(In85, E87, In86),
        ord_add_element(In86, E88, In87),
        ord_add_element(In87, E89, In88),
        ord_add_element(In88, E90, In89),

        ord_add_element(In89, E91, In90),
        ord_add_element(In90, E92, In91),
        ord_add_element(In91, E93, In92),
        ord_add_element(In92, E94, In93),
        ord_add_element(In93, E95, In94),
        ord_add_element(In94, E96, In95),
        ord_add_element(In95, E97, In96),
        ord_add_element(In96, E98, In97),
        ord_add_element(In97, E99, In98),
        ord_add_element(In98, E100, In99),
        osetinsert10(T, In99, Out).

% access
osetaccess([],_).
osetaccess([H|T], OSet):-
        (ord_member(H, OSet) -> true ; true),
        osetaccess(T, OSet).

% access 10
osetaccess10([], _).
osetaccess10([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10|T], OSet):-
        (ord_member(E1, OSet) -> true ; true),
        (ord_member(E2, OSet) -> true ; true),
        (ord_member(E3, OSet) -> true ; true),
        (ord_member(E4, OSet) -> true ; true),
        (ord_member(E5, OSet) -> true ; true),
        (ord_member(E6, OSet) -> true ; true),
        (ord_member(E7, OSet) -> true ; true),
        (ord_member(E8, OSet) -> true ; true),
        (ord_member(E9, OSet) -> true ; true),
        (ord_member(E10, OSet) -> true ; true),
        osetaccess10(T, OSet).

% access 100
osetaccess100([], _).
osetaccess100([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10,
               E11, E12, E13, E14, E15, E16, E17, E18, E19, E20,
               E21, E22, E23, E24, E25, E26, E27, E28, E29, E30,
               E31, E32, E33, E34, E35, E36, E37, E38, E39, E40,
               E41, E42, E43, E44, E45, E46, E47, E48, E49, E50,
               E51, E52, E53, E54, E55, E56, E57, E58, E59, E60,
               E61, E62, E63, E64, E65, E66, E67, E68, E69, E70,
               E71, E72, E73, E74, E75, E76, E77, E78, E79, E80,
               E81, E82, E83, E84, E85, E86, E87, E88, E89, E90,
               E91, E92, E93, E94, E95, E96, E97, E98, E99, E100|T], Oset):-
        (ord_member(E1, Oset) -> true ; true),
        (ord_member(E2, Oset) -> true ; true),
        (ord_member(E3, Oset) -> true ; true),
        (ord_member(E4, Oset) -> true ; true),
        (ord_member(E5, Oset) -> true ; true),
        (ord_member(E6, Oset) -> true ; true),
        (ord_member(E7, Oset) -> true ; true),
        (ord_member(E8, Oset) -> true ; true),
        (ord_member(E9, Oset) -> true ; true),
        (ord_member(E10, Oset) -> true ; true),
        
        (ord_member(E11, Oset) -> true ; true),
        (ord_member(E12, Oset) -> true ; true),
        (ord_member(E13, Oset) -> true ; true),
        (ord_member(E14, Oset) -> true ; true),
        (ord_member(E15, Oset) -> true ; true),
        (ord_member(E16, Oset) -> true ; true),
        (ord_member(E17, Oset) -> true ; true),
        (ord_member(E18, Oset) -> true ; true),
        (ord_member(E19, Oset) -> true ; true),
        (ord_member(E20, Oset) -> true ; true),
        
        (ord_member(E21, Oset) -> true ; true),
        (ord_member(E22, Oset) -> true ; true),
        (ord_member(E23, Oset) -> true ; true),
        (ord_member(E24, Oset) -> true ; true),
        (ord_member(E25, Oset) -> true ; true),
        (ord_member(E26, Oset) -> true ; true),
        (ord_member(E27, Oset) -> true ; true),
        (ord_member(E28, Oset) -> true ; true),
        (ord_member(E29, Oset) -> true ; true),
        (ord_member(E30, Oset) -> true ; true),
        
        (ord_member(E31, Oset) -> true ; true),
        (ord_member(E32, Oset) -> true ; true),
        (ord_member(E33, Oset) -> true ; true),
        (ord_member(E34, Oset) -> true ; true),
        (ord_member(E35, Oset) -> true ; true),
        (ord_member(E36, Oset) -> true ; true),
        (ord_member(E37, Oset) -> true ; true),
        (ord_member(E38, Oset) -> true ; true),
        (ord_member(E39, Oset) -> true ; true),
        (ord_member(E40, Oset) -> true ; true),
        
        (ord_member(E41, Oset) -> true ; true),
        (ord_member(E42, Oset) -> true ; true),
        (ord_member(E43, Oset) -> true ; true),
        (ord_member(E44, Oset) -> true ; true),
        (ord_member(E45, Oset) -> true ; true),
        (ord_member(E46, Oset) -> true ; true),
        (ord_member(E47, Oset) -> true ; true),
        (ord_member(E48, Oset) -> true ; true),
        (ord_member(E49, Oset) -> true ; true),
        (ord_member(E50, Oset) -> true ; true),
        
        (ord_member(E51, Oset) -> true ; true),
        (ord_member(E52, Oset) -> true ; true),
        (ord_member(E53, Oset) -> true ; true),
        (ord_member(E54, Oset) -> true ; true),
        (ord_member(E55, Oset) -> true ; true),
        (ord_member(E56, Oset) -> true ; true),
        (ord_member(E57, Oset) -> true ; true),
        (ord_member(E58, Oset) -> true ; true),
        (ord_member(E59, Oset) -> true ; true),
        (ord_member(E60, Oset) -> true ; true),
        
        (ord_member(E61, Oset) -> true ; true),
        (ord_member(E62, Oset) -> true ; true),
        (ord_member(E63, Oset) -> true ; true),
        (ord_member(E64, Oset) -> true ; true),
        (ord_member(E65, Oset) -> true ; true),
        (ord_member(E66, Oset) -> true ; true),
        (ord_member(E67, Oset) -> true ; true),
        (ord_member(E68, Oset) -> true ; true),
        (ord_member(E69, Oset) -> true ; true),
        (ord_member(E70, Oset) -> true ; true),
        
        (ord_member(E71, Oset) -> true ; true),
        (ord_member(E72, Oset) -> true ; true),
        (ord_member(E73, Oset) -> true ; true),
        (ord_member(E74, Oset) -> true ; true),
        (ord_member(E75, Oset) -> true ; true),
        (ord_member(E76, Oset) -> true ; true),
        (ord_member(E77, Oset) -> true ; true),
        (ord_member(E78, Oset) -> true ; true),
        (ord_member(E79, Oset) -> true ; true),
        (ord_member(E80, Oset) -> true ; true),
        
        (ord_member(E81, Oset) -> true ; true),
        (ord_member(E82, Oset) -> true ; true),
        (ord_member(E83, Oset) -> true ; true),
        (ord_member(E84, Oset) -> true ; true),
        (ord_member(E85, Oset) -> true ; true),
        (ord_member(E86, Oset) -> true ; true),
        (ord_member(E87, Oset) -> true ; true),
        (ord_member(E88, Oset) -> true ; true),
        (ord_member(E89, Oset) -> true ; true),
        (ord_member(E90, Oset) -> true ; true),
        
        (ord_member(E91, Oset) -> true ; true),
        (ord_member(E92, Oset) -> true ; true),
        (ord_member(E93, Oset) -> true ; true),
        (ord_member(E94, Oset) -> true ; true),
        (ord_member(E95, Oset) -> true ; true),
        (ord_member(E96, Oset) -> true ; true),
        (ord_member(E97, Oset) -> true ; true),
        (ord_member(E98, Oset) -> true ; true),
        (ord_member(E99, Oset) -> true ; true),
        (ord_member(E100, Oset) -> true ; true),
        osetaccess100(T, Oset).

% delete
osetdelete([], Out, Out).
osetdelete([H|T], In, Out):-
        ord_del_element(In, H, In2),
        osetdelete(T, In2, Out).

% delete 10
osetdelete10([], Out, Out).
osetdelete10([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10|T], In, Out):-
        ord_del_element(In, E1, In1),
        ord_del_element(In1, E2, In2),
        ord_del_element(In2, E3, In3),
        ord_del_element(In3, E4, In4),
        ord_del_element(In4, E5, In5),
        ord_del_element(In5, E6, In6),
        ord_del_element(In6, E7, In7),
        ord_del_element(In7, E8, In8),
        ord_del_element(In8, E9, In9),
        ord_del_element(In9, E10, In10),
        osetdelete10(T, In10, Out).

% delete 100
osetdelete100([], Out, Out).
osetdelete100([E1, E2, E3, E4, E5, E6, E7, E8, E9, E10,
               E11, E12, E13, E14, E15, E16, E17, E18, E19, E20,
               E21, E22, E23, E24, E25, E26, E27, E28, E29, E30,
               E31, E32, E33, E34, E35, E36, E37, E38, E39, E40,
               E41, E42, E43, E44, E45, E46, E47, E48, E49, E50,
               E51, E52, E53, E54, E55, E56, E57, E58, E59, E60,
               E61, E62, E63, E64, E65, E66, E67, E68, E69, E70,
               E71, E72, E73, E74, E75, E76, E77, E78, E79, E80,
               E81, E82, E83, E84, E85, E86, E87, E88, E89, E90,
               E91, E92, E93, E94, E95, E96, E97, E98, E99, E100|T], In, Out):-
        ord_del_element(In, E1, In1),
        ord_del_element(In1, E2, In2),
        ord_del_element(In2, E3, In3),
        ord_del_element(In3, E4, In4),
        ord_del_element(In4, E5, In5),
        ord_del_element(In5, E6, In6),
        ord_del_element(In6, E7, In7),
        ord_del_element(In7, E8, In8),
        ord_del_element(In8, E9, In9),
        ord_del_element(In9, E10, In10),
        
        ord_del_element(In10, E11, In11),
        ord_del_element(In11, E12, In12),
        ord_del_element(In12, E13, In13),
        ord_del_element(In13, E14, In14),
        ord_del_element(In14, E15, In15),
        ord_del_element(In15, E16, In16),
        ord_del_element(In16, E17, In17),
        ord_del_element(In17, E18, In18),
        ord_del_element(In18, E19, In19),
        ord_del_element(In19, E20, In20),

        ord_del_element(In20, E21, In21),
        ord_del_element(In21, E22, In22),
        ord_del_element(In22, E23, In23),
        ord_del_element(In23, E24, In24),
        ord_del_element(In24, E25, In25),
        ord_del_element(In25, E26, In26),
        ord_del_element(In26, E27, In27),
        ord_del_element(In27, E28, In28),
        ord_del_element(In28, E29, In29),
        ord_del_element(In29, E30, In30),

        ord_del_element(In30, E31, In31),
        ord_del_element(In31, E32, In32),
        ord_del_element(In32, E33, In33),
        ord_del_element(In33, E34, In34),
        ord_del_element(In34, E35, In35),
        ord_del_element(In35, E36, In36),
        ord_del_element(In36, E37, In37),
        ord_del_element(In37, E38, In38),
        ord_del_element(In38, E39, In39),
        ord_del_element(In39, E40, In40),

        ord_del_element(In40, E41, In41),
        ord_del_element(In41, E42, In42),
        ord_del_element(In42, E43, In43),
        ord_del_element(In43, E44, In44),
        ord_del_element(In44, E45, In45),
        ord_del_element(In45, E46, In46),
        ord_del_element(In46, E47, In47),
        ord_del_element(In47, E48, In48),
        ord_del_element(In48, E49, In49),
        ord_del_element(In49, E50, In50),

        ord_del_element(In50, E51, In51),
        ord_del_element(In51, E52, In52),
        ord_del_element(In52, E53, In53),
        ord_del_element(In53, E54, In54),
        ord_del_element(In54, E55, In55),
        ord_del_element(In55, E56, In56),
        ord_del_element(In56, E57, In57),
        ord_del_element(In57, E58, In58),
        ord_del_element(In58, E59, In59),
        ord_del_element(In59, E60, In60),

        ord_del_element(In60, E61, In61),
        ord_del_element(In61, E62, In62),
        ord_del_element(In62, E63, In63),
        ord_del_element(In63, E64, In64),
        ord_del_element(In64, E65, In65),
        ord_del_element(In65, E66, In66),
        ord_del_element(In66, E67, In67),
        ord_del_element(In67, E68, In68),
        ord_del_element(In68, E69, In69),
        ord_del_element(In69, E70, In70),

        ord_del_element(In70, E71, In71),
        ord_del_element(In71, E72, In72),
        ord_del_element(In72, E73, In73),
        ord_del_element(In73, E74, In74),
        ord_del_element(In74, E75, In75),
        ord_del_element(In75, E76, In76),
        ord_del_element(In76, E77, In77),
        ord_del_element(In77, E78, In78),
        ord_del_element(In78, E79, In79),
        ord_del_element(In79, E80, In80),

        ord_del_element(In80, E81, In81),
        ord_del_element(In81, E82, In82),
        ord_del_element(In82, E83, In83),
        ord_del_element(In83, E84, In84),
        ord_del_element(In84, E85, In85),
        ord_del_element(In85, E86, In86),
        ord_del_element(In86, E87, In87),
        ord_del_element(In87, E88, In88),
        ord_del_element(In88, E89, In89),
        ord_del_element(In89, E90, In90),

        ord_del_element(In90, E91, In91),
        ord_del_element(In91, E92, In92),
        ord_del_element(In92, E93, In93),
        ord_del_element(In93, E94, In94),
        ord_del_element(In94, E95, In95),
        ord_del_element(In95, E96, In96),
        ord_del_element(In96, E97, In97),
        ord_del_element(In97, E98, In98),
        ord_del_element(In98, E99, In99),
        ord_del_element(In99, E100, In100),

        osetdelete100(T, In100, Out).

% clear
osetclear(OrderedSet, OrderedSetClear):-
        osetdelete(OrderedSet, OrderedSet, OrderedSetClear).