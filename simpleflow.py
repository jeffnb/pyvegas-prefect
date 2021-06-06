from datetime import datetime, timedelta
from typing import List

from prefect import task, Flow, Parameter
from prefect.executors import LocalDaskExecutor
from prefect.run_configs import LocalRun

@task
def reverse_names(name_list: List[str]) -> List[str]:
    """
    Returns a list of strings reversed
    """
    return [name[::-1] for name in name_list]

@task
def add_characters(name_list: List[str]) -> int:
    """
    Add up all the characters in this list
    """
    return sum([len(name) for name in name_list])

@task
def count_names(name_list: List[str]) -> int:
    """
    Return len of the list
    """
    return len(name_list)

@task
def duplicate_list(name_list: List[str], count: int) -> List[str]:
    """
    Return a list
    """
    return [name * count for name in name_list]


with Flow("PyVegas Flow", executor=LocalDaskExecutor()) as flow:
    name_list = Parameter("names", default=["Adam", "Chris", "Benny", "Tom", "Alice"])

    reverse_names = reverse_names(name_list)
    char_sum = add_characters(reverse_names)
    name_count = count_names(reverse_names)

    final_list = duplicate_list(reverse_names, char_sum+name_count)


if __name__ == '__main__':
    # flow.register("Testing", labels=["temporary"])
    # flow.visualize()
    #state = flow.run(names=["Foo", "Bar", "Baz"])
    # print(state)
    flow.register("Testing", labels=["temporary"])
