import visualizer


def bench_access_integer():
    # Data structure size 1 to 100 for operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_SmallDataStructures_Integer", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutarray", "Mutarray", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Small_Data_Structures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.5,
    })
    df_manager.plot_simple({
        "figure_name": "Access_Small_Data_Structures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.1,
    })

    # Data Structure Size 1 to 10.000 with operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_BigDataStructures_Integer", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutarray", "Mutarray", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 45,
    })
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.2,
    })

    # Miss chance from 0 to 100 for data structure size 10.000 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Integer", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Integer_Closeup(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.2,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Integer", [
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Integer(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 60,
    })

    # Miss chance from 0 to 100 for data structure size 10 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Integer_10", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Integer(Data_Structure_Size_10_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.08,
    })

    # Miss chance from 0 to 100 for data structure size 15 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Integer_15", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss"),
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Integer(Data_Structure_Size_15_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.1,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OperationCount", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutarray", "Mutarray", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_Integer(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 45,
    })
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_Integer_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.2,
    })


def bench_memory_access_integer():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray hit", "garbage_collector_calls_hit"),
        ("mutarray", "Mutarray miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 70,
    })
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 12500,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray hit", "garbage_collector_calls_hit"),
        ("mutarray", "Mutarray miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 120,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray hit", "garbage_collector_calls_hit"),
        ("mutarray", "Mutarray miss", "garbage_collector_calls_miss"),
    ])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 120,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray hit", "global_stack_access"),
        ("mutarray", "Mutarray miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 3500000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray hit", "global_stack_access"),
        ("mutarray", "Mutarray miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 3500000,
    })
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
    ])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_IntegerP3(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 3500000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray hit", "global_stack_access"),
        ("mutarray", "Mutarray miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutarray", ["Mutarray init", "Mutarray hit", "Mutarray miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_BigDataStructures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 35000000,
    })


def bench_insert_integer():
    # Data structure size 1 to 100 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_SmallDataStructures", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutarray", "Mutarray", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List (no duplicates)", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Small_Data_Structures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.8,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_Small_Data_Structures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.3,
    })

    # Data structure size 1 to 10.000 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_BigDataStructures_Integer", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutarray", "Mutarray", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List (no duplicates)", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 80,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.65,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_OperationCount", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutarray", "Mutarray", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List (no duplicates)", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_Integer(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 80,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_Integer_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.65,
    })


def bench_memory_insert_integer():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 15,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 4000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 20,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
    ])
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 20,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("mutarray", "Mutarray init", "garbage_collector_calls_init"),
        ("mutarray", "Mutarray insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
    ])
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_IntegerP3(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 20,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard insert", "global_stack_insert"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_IntegerP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 40000000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard insert", "global_stack_insert"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
    ])
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_IntegerP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 40000000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
    ])
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_Integer_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard insert", "global_stack_insert"),
        ("mutarray", "Mutarray init", "global_stack_init"),
        ("mutarray", "Mutarray insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutarray", "Mutarray init", "Mutarray insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutarray", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_BigDataStructures_Integer(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 100000000,
    })


def bench_access_complex():
    # Data structure size 1 to 100 with operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Small_Data_Structures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    # Data Structure Size 1 to 10.000 with operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_BigDataStructures_ComplexTerms", [
        ("avl", "AVL", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_ComplexTerms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })

    # Miss percentage 0 to 100 with data structure size 10.000 and operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_ComplexTerms", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_ComplexTerms_Closeup(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_ComplexTerms", [
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_ComplexTerms(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })

    # Miss percentage 0 to 100 with data structure size 10 and operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_ComplexTerms_10", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_ComplexTerms(Data_Structure_Size_10_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.15,
    })

    # Miss percentage 0 to 100 with data structure size 15 and operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_ComplexTerms_15", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_ComplexTerms(Data_Structure_Size_15_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.3,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OperationCount_ComplexTerms", [
        ("avl", "AVL", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_ComplexTerms(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_ComplexTerms_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })


def bench_memory_access_complex():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 15,
    })
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_ComplexTermsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 7000,
    })
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 40,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_ComplexTerms", [
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
    ])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_ComplexTermsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 40,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 18000000,
    })
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_ComplexTerms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_BigDataStructures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 18000000,
    })


def bench_insert_complex():
    # Data structure size 1 to 100 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Small_Data_Structures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 1.5,
    })

    # Data structure size 1 to 10.000 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_BigDataStructures_ComplexTerms", [
        ("avl", "AVL", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert")
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 140,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_ComplexTerms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.8,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_OperationCount_ComplexTerms", [
        ("avl", "AVL", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert")
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_ComplexTerms(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 130,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_ComplexTerms_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.8,
    })


def bench_memory_insert_complex():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 15,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_ComplexTermsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1500,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_ComplexTerms", [
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
    ])
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_ComplexTermsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_ComplexTerms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_ComplexTermsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 17500000,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_ComplexTerms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_BigDataStructures_ComplexTerms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 150000000,
    })


def bench_insert_atoms():
    # Data structure size 1 to 100 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_SmallDataStructures_Atoms", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Small_Data_Structures_Atoms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 1.8,
    })

    # Data structure size 1 to 10.000 with constant operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_BigDataStructures_Atoms", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_Atoms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 160,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_Big_Data_Structures_Atoms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.75,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_OperationCount_Atoms", [
        ("avl", "AVL", "insert"),
        ("blackboard", "Blackboard", "insert"),
        ("mutdict", "Mutdict", "insert"),
        ("assertds", "Assert", "insert"),
        ("list", "List", "insert"),
        ("orderedset", "Ordered Set", "insert"),
        ("list_without_duplicates", "List without duplicates", "insert")
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_Atoms(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 150,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_OpCount_Atoms_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.8,
    })


def bench_memory_insert_atoms():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 15,
    })
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_BigDataStructures_AtomsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 4000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL insert", "garbage_collector_calls_insert"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict insert", "garbage_collector_calls_insert"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert insert", "garbage_collector_calls_insert"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set insert", "garbage_collector_calls_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 30,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard insert", "garbage_collector_calls_insert"),
        ("list_without_duplicates", "List no duplicates init", "garbage_collector_calls_init"),
        ("list_without_duplicates", "List no duplicates insert", "garbage_collector_calls_insert"),
    ])
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GarbageCollectionCount_SmallDataStructures_AtomsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 30,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 35000000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert")
    ])
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_Atoms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert")
    ])
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.multiply_column("List", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_SmallDataStructures_AtomsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 35000000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL insert", "global_stack_insert"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard insert", "global_stack_insert"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict insert", "global_stack_insert"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert insert", "global_stack_insert"),
        ("list", "List init", "global_stack_init"),
        ("list", "List insert", "global_stack_insert"),
        ("list_without_duplicates", "List no duplicates init", "global_stack_init"),
        ("list_without_duplicates", "List no duplicates insert", "global_stack_insert"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set insert", "global_stack_insert")
    ])
    df_manager.combine_columns("AVL", "AVL init", "AVL insert")
    df_manager.combine_columns("Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.combine_columns("Mutdict", "Mutdict init", "Mutdict insert")
    df_manager.combine_columns("Assert", "Assert init", "Assert insert")
    df_manager.combine_columns("List", "List init", "List insert")
    df_manager.combine_columns("List no duplicates", "List no duplicates init", "List no duplicates insert")
    df_manager.combine_columns("Ordered Set", "Ordered Set init", "Ordered Set insert")
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("List no duplicates", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_GlobalStack_BigDataStructures_Atoms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 100000000,
    })


def bench_access_atoms():
    # Data structure size 1 to 100 for operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_SmallDataStructures_Atoms", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Small_Data_Structures_Atoms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.8,
    })

    # Data Structure Size 1 to 10.000 with operation count 1.000.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_BigDataStructures_Atoms", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_Atoms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 120,
    })
    df_manager.plot_simple({
        "figure_name": "Access_Big_Data_Structures_Atoms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })

    # Miss chance from 0 to 100 for data structure size 10.000 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Atoms", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Atoms_Closeup(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Atoms", [
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Atoms(Data_Structure_Size_10000_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 125,
    })

    # Miss chance from 0 to 100 for data structure size 10 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Atoms_10", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Atoms(Data_Structure_Size_10_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.15,
    })

    # Miss chance from 0 to 100 for data structure size 15 and operation count 1.000.000.
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_MissChance_Atoms_15", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss"),
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_MissChance_Atoms(Data_Structure_Size_15_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.175,
    })

    # Operation count from 0 to 1.000.000 data structure size 10.000
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OperationCount_Atoms", [
        ("avl", "AVL", "access"),
        ("blackboard", "Blackboard", "access"),
        ("mutdict", "Mutdict", "access"),
        ("assertds", "Assert", "access"),
        ("list", "List", "access"),
        ("orderedset", "Ordered Set", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_Atoms(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })
    df_manager.plot_simple({
        "figure_name": "Access_OpCount_Atoms_Closeup(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.4,
    })


def bench_memory_access_atoms():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_BigDataStructures_AtomsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 2500,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Atoms", [
        ("avl", "AVL init", "garbage_collector_calls_init"),
        ("avl", "AVL hit", "garbage_collector_calls_hit"),
        ("avl", "AVL miss", "garbage_collector_calls_miss"),
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
        ("mutdict", "Mutdict init", "garbage_collector_calls_init"),
        ("mutdict", "Mutdict hit", "garbage_collector_calls_hit"),
        ("mutdict", "Mutdict miss", "garbage_collector_calls_miss"),
        ("assertds", "Assert init", "garbage_collector_calls_init"),
        ("assertds", "Assert hit", "garbage_collector_calls_hit"),
        ("assertds", "Assert miss", "garbage_collector_calls_miss"),
        ("list", "List init", "garbage_collector_calls_init"),
        ("list", "List hit", "garbage_collector_calls_hit"),
        ("list", "List miss", "garbage_collector_calls_miss"),
        ("orderedset", "Ordered Set init", "garbage_collector_calls_init"),
        ("orderedset", "Ordered Set hit", "garbage_collector_calls_hit"),
        ("orderedset", "Ordered Set miss", "garbage_collector_calls_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 150,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Atoms", [
        ("blackboard", "Blackboard init", "garbage_collector_calls_init"),
        ("blackboard", "Blackboard hit", "garbage_collector_calls_hit"),
        ("blackboard", "Blackboard miss", "garbage_collector_calls_miss"),
    ])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GarbageCollectionCount_SmallDataStructures_AtomsP2(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Garbage Collector Calls",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 150,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Atoms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_AtomsP1(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 3000000,
    })
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_SmallDataStructures_Atoms_Closeup(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 5000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("avl", "AVL init", "global_stack_init"),
        ("avl", "AVL hit", "global_stack_access"),
        ("avl", "AVL miss", "global_stack_miss"),
        ("blackboard", "Blackboard init", "global_stack_init"),
        ("blackboard", "Blackboard hit", "global_stack_access"),
        ("blackboard", "Blackboard miss", "global_stack_miss"),
        ("mutdict", "Mutdict init", "global_stack_init"),
        ("mutdict", "Mutdict hit", "global_stack_access"),
        ("mutdict", "Mutdict miss", "global_stack_miss"),
        ("assertds", "Assert init", "global_stack_init"),
        ("assertds", "Assert hit", "global_stack_access"),
        ("assertds", "Assert miss", "global_stack_miss"),
        ("list", "List init", "global_stack_init"),
        ("list", "List hit", "global_stack_access"),
        ("list", "List miss", "global_stack_miss"),
        ("orderedset", "Ordered Set init", "global_stack_init"),
        ("orderedset", "Ordered Set hit", "global_stack_access"),
        ("orderedset", "Ordered Set miss", "global_stack_miss")
    ])
    df_manager.combine_multiple_columns("AVL", ["AVL init", "AVL hit", "AVL miss"])
    df_manager.combine_multiple_columns("Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Mutdict", ["Mutdict init", "Mutdict hit", "Mutdict miss"])
    df_manager.combine_multiple_columns("Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.combine_multiple_columns("List", ["List init", "List hit", "List miss"])
    df_manager.combine_multiple_columns("Ordered Set", ["Ordered Set init", "Ordered Set hit", "Ordered Set miss"])
    df_manager.multiply_column("AVL", 1000)
    df_manager.multiply_column("Blackboard", 1000)
    df_manager.multiply_column("Mutdict", 1000)
    df_manager.multiply_column("Assert", 1000)
    df_manager.multiply_column("List", 1000)
    df_manager.multiply_column("Ordered Set", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_GlobalStack_BigDataStructures_Atoms(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes Used",
        "x_lim_lower": 0, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 35000000,
    })


def bench_walltime_runtime_comparison():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OperationCount_ComplexTerms", [
        ("orderedset", "Ordered Set Runtime", "runtime_access"),
        ("orderedset", "Ordered Set Walltime", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Runtime_Walltime_OpCount_ComplexTerms(Data_Structure_Size_10000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })


def bench_orderedset1_10_100_comparison():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OrderedSet1_10_100_Comparison", [
        ("orderedset", "Ordered Set 1", "access"),
        ("orderedset10", "Ordered Set 10", "access"),
        ("orderedset100", "Ordered Set 100", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_OrderedSet1_10_100_Comparison(Data_Structure_Size_1000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 4.2,
    })


def bench_loop_overhead():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchAccess_OrderedSet1_10_100_Comparison", [
        ("orderedset", "Access Time", "access"),
        ("orderedset", "Loop Time", "emptyloop")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Loop_Overhead(Data_Structure_Size_1000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 4.2,
    })


def bench_heap():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard hit", "heap_access"),
        ("blackboard", "Blackboard miss", "heap_miss"),
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert hit", "heap_access"),
        ("assertds", "Assert miss", "heap_miss")
    ])
    df_manager.combine_multiple_columns("Integer Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Integer Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.multiply_column("Integer Blackboard", 1000)
    df_manager.multiply_column("Integer Assert", 1000)
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_Atoms", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard hit", "heap_access"),
        ("blackboard", "Blackboard miss", "heap_miss"),
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert hit", "heap_access"),
        ("assertds", "Assert miss", "heap_miss")
    ])
    df_manager.combine_multiple_columns("Atoms Blackboard", ["Blackboard init", "Blackboard hit", "Blackboard miss"])
    df_manager.combine_multiple_columns("Atoms Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.multiply_column("Atoms Blackboard", 1000)
    df_manager.multiply_column("Atoms Assert", 1000)
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_SmallDataStructures_ComplexTerms", [
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert hit", "heap_access"),
        ("assertds", "Assert miss", "heap_miss")
    ])
    df_manager.combine_multiple_columns("Complex Terms Assert", ["Assert init", "Assert hit", "Assert miss"])
    df_manager.multiply_column("Complex Terms Assert", 1000)
    df_manager.plot_simple({
        "figure_name": "Access_Heap_SmallDataStructures(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 25000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard insert", "heap_insert"),
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert insert", "heap_insert")
    ])
    df_manager.combine_columns("Integer Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.multiply_column("Integer Blackboard", 1000)
    df_manager.combine_columns("Integer Assert", "Assert init", "Assert insert")
    df_manager.multiply_column("Integer Assert", 1000)
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard insert", "heap_insert"),
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert insert", "heap_insert")
    ])
    df_manager.combine_columns("Atoms Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.multiply_column("Atoms Blackboard", 1000)
    df_manager.combine_columns("Atoms Assert", "Assert init", "Assert insert")
    df_manager.multiply_column("Atoms Assert", 1000)
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_ComplexTerms", [
        ("assertds", "Assert init", "heap_init"),
        ("assertds", "Assert insert", "heap_insert")
    ])
    df_manager.combine_columns("Complex Terms Assert", "Assert init", "Assert insert")
    df_manager.multiply_column("Complex Terms Assert", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_Heap_SmallDataStructures(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 250000000,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Integer", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard insert", "heap_insert")
    ])
    df_manager.combine_columns("Integer Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.multiply_column("Integer Blackboard", 1000)
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_SmallDataStructures_Atoms", [
        ("blackboard", "Blackboard init", "heap_init"),
        ("blackboard", "Blackboard insert", "heap_insert")
    ])
    df_manager.combine_columns("Atoms Blackboard", "Blackboard init", "Blackboard insert")
    df_manager.multiply_column("Atoms Blackboard", 1000)
    df_manager.plot_simple({
        "figure_name": "Insert_Heap_SmallDataStructures_BlackBoard(Operation_Count_1000000)",
        "x_label": "Data Structure Size", "y_label": "Bytes",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 20000,
    })


def bench_avl_avlfchk():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_Avl_fchk_OperationCount", [
        ("avl", "AVL", "insert"),
        ("avl_fchk", "AVL with fetch check", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_AVL_fchk_OpCount(Data_Structure_Size_100000)",
        "x_label": "Operation Count", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 1000000,
        "y_lim_lower": 0, "y_lim_upper": 0.12,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/BenchInsert_Avl_fchk_DataStructureSize", [
        ("avl", "AVL", "insert"),
        ("avl_fchk", "AVL with fetch check", "insert"),
    ])
    df_manager.plot_simple({
        "figure_name": "Insert_AVL_fchk_DsSize(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.3,
    })


def bench_ordered_set_gc_time():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("orderedset", "orderedset access", "access"),
        ("orderedset", "orderedset gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "orderedset gc", "orderedset access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("orderedset", "orderedset access", "access"),
        ("orderedset", "orderedset gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "orderedset gc", "orderedset access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("orderedset", "orderedset access", "access"),
        ("orderedset", "orderedset gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Complex Terms", "orderedset gc", "orderedset access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("orderedset", "orderedset insert", "insert"),
        ("orderedset", "orderedset gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "orderedset gc", "orderedset insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("orderedset", "orderedset insert", "insert"),
        ("orderedset", "orderedset gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "orderedset gc", "orderedset insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("orderedset", "orderedset insert", "insert"),
        ("orderedset", "orderedset gc", "garbage_collection_insert")
    ])

    df_manager.percentage_of("Insert Complex Terms", "orderedset gc", "orderedset insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_OrderedSet(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("list", "list access", "access"),
        ("list", "list gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "list gc", "list access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("list", "list access", "access"),
        ("list", "list gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "list gc", "list access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("list", "list access", "access"),
        ("list", "list gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("AccessComplex Terms", "list gc", "list access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("list", "list insert", "insert"),
        ("list", "list gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "list gc", "list insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("list", "list insert", "insert"),
        ("list", "list gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "list gc", "list insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("list", "list insert", "insert"),
        ("list", "list gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Complex Terms", "list gc", "list insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_List(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("avl", "avl access", "access"),
        ("avl", "avl gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "avl gc", "avl access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("avl", "avl access", "access"),
        ("avl", "avl gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "avl gc", "avl access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("avl", "avl access", "access"),
        ("avl", "avl gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Complex Terms", "avl gc", "avl access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("avl", "avl insert", "insert"),
        ("avl", "avl gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "avl gc", "avl insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("avl", "avl insert", "insert"),
        ("avl", "avl gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "avl gc", "avl insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("avl", "avl insert", "insert"),
        ("avl", "avl gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Complex Terms", "avl gc", "avl insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_AVL(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("mutarray", "mutarray access", "access"),
        ("mutarray", "mutarray gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "mutarray gc", "mutarray access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("mutarray", "mutarray insert", "insert"),
        ("mutarray", "mutarray gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "mutarray gc", "mutarray insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_Mutarray(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("mutdict", "mutdict access", "access"),
        ("mutdict", "mutdict gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "mutdict gc", "mutdict access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("mutdict", "mutdict access", "access"),
        ("mutdict", "mutdict gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "mutdict gc", "mutdict access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("mutdict", "mutdict access", "access"),
        ("mutdict", "mutdict gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Complex Terms", "mutdict gc", "mutdict access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("mutdict", "mutdict insert", "insert"),
        ("mutdict", "mutdict gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "mutdict gc", "mutdict insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("mutdict", "mutdict insert", "insert"),
        ("mutdict", "mutdict gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "mutdict gc", "mutdict insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("mutdict", "mutdict insert", "insert"),
        ("mutdict", "mutdict gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Complex Terms", "mutdict gc", "mutdict insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_Mutdict(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("assertds", "assert access", "access"),
        ("assertds", "assert gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "assert gc", "assert access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("assertds", "assert access", "access"),
        ("assertds", "assert gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "assert gc", "assert access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_ComplexTerms", [
        ("assertds", "assert access", "access"),
        ("assertds", "assert gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Complex Terms", "assert gc", "assert access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("assertds", "assert insert", "insert"),
        ("assertds", "assert gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "assert gc", "assert insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("assertds", "assert insert", "insert"),
        ("assertds", "assert gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "assert gc", "assert insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_ComplexTerms", [
        ("assertds", "assert insert", "insert"),
        ("assertds", "assert gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Complex Terms", "assert gc", "assert insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_Assert(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Integer", [
        ("blackboard", "blackboard access", "access"),
        ("blackboard", "blackboard gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Integer", "blackboard gc", "blackboard access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("blackboard", "blackboard access", "access"),
        ("blackboard", "blackboard gc", "garbage_collection_hit")
    ])
    df_manager.percentage_of("Access Atoms", "blackboard gc", "blackboard access")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Integer", [
        ("blackboard", "blackboard insert", "insert"),
        ("blackboard", "blackboard gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Integer", "blackboard gc", "blackboard insert")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryInsert_BigDataStructures_Atoms", [
        ("blackboard", "blackboard insert", "insert"),
        ("blackboard", "blackboard gc", "garbage_collection_insert")
    ])
    df_manager.percentage_of("Insert Atoms", "blackboard gc", "blackboard insert")
    df_manager.plot_simple({
        "figure_name": "Access_GCTime_Blackboard(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Proportion of the runtime",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 1,
    })


def bench_random_number_comp():
    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/RandomSeed1234_BenchAccess_BigDataStructures_Atoms", [
        ("orderedset", "Ordered Set 1234", "access"),
        ("list", "List 1234", "access")
    ])
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("orderedset", "Ordered Set 42", "access"),
        ("list", "List 42", "access")
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Randomnumber_ComparisonP1(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 100,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/RandomSeed1234_BenchAccess_BigDataStructures_Atoms", [
        ("avl", "AVL 1234", "access"),
        ("blackboard", "Blackboard 1234", "access"),
    ])
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("avl", "AVL 42", "access"),
        ("blackboard", "Blackboard 42", "access"),
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Randomnumber_ComparisonP2(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.5,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/RandomSeed1234_BenchAccess_BigDataStructures_Atoms", [
        ("mutdict", "Mutdict 1234", "access"),
        ("assertds", "Assert 1234", "access"),
    ])
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/MemoryAccess_BigDataStructures_Atoms", [
        ("mutdict", "Mutdict 42", "access"),
        ("assertds", "Assert 42", "access"),
    ])
    df_manager.plot_simple({
        "figure_name": "Access_Randomnumber_ComparisonP3(OpCount_1000000)",
        "x_label": "Data Structure Size", "y_label": "Time in Seconds",
        "x_lim_lower": 1, "x_lim_upper": 10000,
        "y_lim_lower": 0, "y_lim_upper": 0.5,
    })

    df_manager: visualizer.DataFrameManager = visualizer.DataFrameManager("Sample Size")
    df_manager.add_data_from_folder("../Prolog/Benchmark/results/RandomSeed1234_BenchAccess_MissChance_Atoms_10", [
        ("avl", "AVL Hit", "access"),
        ("avl", "AVL Miss", "access_miss"),
        ("blackboard", "Blackboard Hit", "access"),
        ("blackboard", "Blackboard Miss", "access_miss"),
        ("mutdict", "Mutdict Hit", "access"),
        ("mutdict", "Mutdict Miss", "access_miss"),
        ("assertds", "Assert Hit", "access"),
        ("assertds", "Assert Miss", "access_miss"),
        ("list", "List Hit", "access"),
        ("list", "List Miss", "access_miss"),
        ("orderedset", "Ordered Set Hit", "access"),
        ("orderedset", "Ordered Set Miss", "access_miss")
    ])
    df_manager.combine_columns("AVL", "AVL Hit", "AVL Miss")
    df_manager.combine_columns("Blackboard", "Blackboard Hit", "Blackboard Miss")
    df_manager.combine_columns("Mutdict", "Mutdict Hit", "Mutdict Miss")
    df_manager.combine_columns("Assert", "Assert Hit", "Assert Miss")
    df_manager.combine_columns("List", "List Hit", "List Miss")
    df_manager.combine_columns("Ordered Set", "Ordered Set Hit", "Ordered Set Miss")
    df_manager.plot_simple({
        "figure_name": "Access_Randomnumber_ComparisonP4(Data_Structure_Size_10_Operation_Count_1000000)",
        "x_label": "Miss Chance in Percent", "y_label": "Time in Seconds",
        "x_lim_lower": 0, "x_lim_upper": 100,
        "y_lim_lower": 0, "y_lim_upper": 0.15,
    })


if __name__ == '__main__':
    # Access Operation
    bench_access_complex()
    bench_access_integer()
    bench_access_atoms()
    bench_memory_access_integer()
    bench_memory_access_atoms()
    bench_memory_access_complex()

    # Insert operation
    bench_insert_complex()
    bench_insert_integer()
    bench_insert_atoms()
    bench_memory_insert_integer()
    bench_memory_insert_atoms()
    bench_memory_insert_complex()

    # Other Memory
    bench_heap()
    bench_ordered_set_gc_time()

    # Other
    bench_random_number_comp()
    bench_loop_overhead()
    bench_avl_avlfchk()
    bench_walltime_runtime_comparison()
    bench_orderedset1_10_100_comparison()
    bench_walltime_runtime_comparison()
