import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re


class DataFrameManager:
    def __init__(self, sample_size_label: str):
        self.__sample_size_label: str = sample_size_label
        self.__df: pd.DataFrame = pd.DataFrame({sample_size_label: []})

    def __compress_data(self, df: pd.DataFrame, label: str, col_name: str) -> pd.DataFrame:
        # Select columns with label
        target_df = df.filter(regex=f'^{label}_[0-9]+', axis=1)
        if target_df.empty:
            return pd.DataFrame()

        # Calculate geometric means
        # Remove negative values
        target_df.values[target_df.values < 0] = 0

        # 1 is added before and subtracted after the calculation to deal with values equal to 0.
        exponent: float = 1 / len(target_df.values[0])

        row_products: np.array = np.prod(np.add(target_df.values, 1), axis=1)
        compressed_data: np.array = np.subtract(np.power(row_products, exponent), 1)

        return pd.DataFrame({
            self.__sample_size_label: df[self.__sample_size_label],
            col_name: compressed_data
        })

    def __update_sample_size(self, df: pd.DataFrame):
        new_sample_sizes = list(filter(lambda x: x not in self.__df[self.__sample_size_label].values, df[self.__sample_size_label]))
        sample_sizes_df: pd.DataFrame = pd.DataFrame({self.__sample_size_label: new_sample_sizes})
        self.__df = pd.concat([self.__df, sample_sizes_df], ignore_index=True)
        self.__df = self.__df.sort_values(by=[self.__sample_size_label], axis=0, ignore_index=True)

    def __insert_new_data(self, df: pd.DataFrame, column_number: int = 1):
        self.__df = pd.concat([self.__df, df.iloc[:, column_number:]], axis=1)

    def __remove_col(self, col_name: str):
        self.__df.drop(col_name, inplace=True, axis=1)

    def percentage_of(self, new_col_name: str, col_name1: str, col_name2: str):
        df1: pd.DataFrame = self.__df.filter(regex=f'^{col_name1}$', axis=1)
        df2: pd.DataFrame = self.__df.filter(regex=f'^{col_name2}$', axis=1)
        percent_df: pd.DataFrame = np.divide(df1, np.asarray(df2))
        self.__remove_col(col_name1)
        self.__remove_col(col_name2)
        percent_df = percent_df.fillna(0)
        percent_df = percent_df.rename(columns={col_name1: new_col_name})
        self.__insert_new_data(percent_df, 0)

    def combine_columns(self, new_col_name: str, col_name1: str, col_name2: str):
        df1: pd.DataFrame = self.__df.filter(regex=f'^{col_name1}$', axis=1)
        df2: pd.DataFrame = self.__df.filter(regex=f'^{col_name2}$', axis=1)
        sum_df: pd.DataFrame = np.add(df1, np.asarray(df2))
        self.__remove_col(col_name1)
        self.__remove_col(col_name2)
        sum_df = sum_df.rename(columns={col_name1: new_col_name})
        self.__insert_new_data(sum_df, 0)

    def combine_multiple_columns(self, new_col_name: str, col_names: list):
        while len(col_names) > 2:
            col_name1: str = col_names[0]
            col_name2: str = col_names[1]
            col_names.remove(col_name2)
            self.combine_columns(col_name1, col_name1, col_name2)
        col_name1: str = col_names[0]
        col_name2: str = col_names[1]
        self.combine_columns(new_col_name, col_name1, col_name2)

    def subtract_columns(self, new_col_name: str, col_name1: str, col_name2: str):
        df1: pd.DataFrame = self.__df.filter(regex=f'^{col_name1}$', axis=1)
        df2: pd.DataFrame = self.__df.filter(regex=f'^{col_name2}$', axis=1)
        sub_df: pd.DataFrame = np.subtract(df1, df2)
        self.__remove_col(col_name1)
        self.__remove_col(col_name2)
        sub_df = sub_df.rename(columns={col_name1: new_col_name})
        self.__insert_new_data(sub_df, 0)

    def multiply_column(self, col_name: str, factor: float):
        df: pd.DataFrame = self.__df.filter(regex=f'^{col_name}$', axis=1)
        mul_df: pd.DataFrame = np.multiply(df, factor)
        self.__remove_col(col_name)
        self.__insert_new_data(mul_df, 0)

    def add_data(self, file_name: str, col_name: str, label: str):
        csv_df: pd.DataFrame = pd.read_csv(file_name, sep=',', header=0)
        df: pd.DataFrame = self.__compress_data(csv_df, label, col_name)
        self.__update_sample_size(df)
        self.__insert_new_data(df)

    def add_data_from_folder(self, folder_path: str, name_mapping: list):
        files = os.listdir(folder_path)

        for (data_structure_name, col_name, label) in name_mapping:
            for file_name in files:
                file_data_structure_name: str = re.split("__", file_name)[0]
                if data_structure_name != file_data_structure_name:
                    continue
                complete_path: str = folder_path + "/" + file_name
                self.add_data(complete_path, col_name, label)
                break

    def plot_simple(self, plot_info: dict):
        plt.close("all")
        font = {'family': 'DejaVu Sans', 'size': 14}
        plt.rc('font', **font)

        figure_name: str = plot_info["figure_name"]
        x_label: str = plot_info["x_label"]
        y_label: str = plot_info["y_label"]
        x_lim_lower: int = plot_info["x_lim_lower"]
        x_lim_upper: int = plot_info["x_lim_upper"]
        y_lim_lower: int = plot_info["y_lim_lower"]
        y_lim_upper: int = plot_info["y_lim_upper"]

        opacity: float = 1.0
        if "opacity" in plot_info:
            opacity = plot_info["opacity"]

        self.__df.plot(x=self.__sample_size_label, xlabel=x_label, ylabel=y_label, alpha=opacity)
        plt.ylim(y_lim_lower, y_lim_upper)
        plt.xlim(x_lim_lower, x_lim_upper)
        plt.plot()
        plt.savefig(f"fig/{figure_name}")

    def print_df(self):
        print(self.__df.to_string())
