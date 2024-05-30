[назад](/README.md)

# Соглашение по коду

> Код — это средство передачи информации, и в первую очередь другим людям, а не компьютерам. ( *Дэвид Фарли* )

# Общие положения:
1. __Код должен читаться сверху вниз как рассказ__ в порядке выполнения функциональности.
2. __Переменные/функции/классы/модули должны иметь понятное название__, которое должно быть написано человеческим языком и отражать суть в полной мере (функции = глаголы, переменные/классы/модули = существительные/прилагательные).
3. __Функции/классы/модули должны быть атомарными__, то есть выполнять только одну задачу.
4. __Функции/классы/модули не должны зависеть друг от друга__ (внесение изменений в одном модуле не должно повлечь за собой необходимость внесения изменений в другом).
5. Необходимо __дать другому разработчику максимум информации__ о том, как работает функция/класс/модуль и __избавить его от необходимости погружаться в логику работы__ функции/класса/модуля.

# Теперь конкретнее:
1. Импортируем только используемые модули в таком порядке:
	```python
	import os                                   # 1.1 модули из стандартной библиотеки
	import math as mth                          # 1.2
	from statistics import mean                 # 1.3
	from dataclasses import dataclass as dtc    # 1.4
	import panadas                              # 2.1 внешние модули
	import numpy as np                          # 2.2
	from networkx import eigenvector_centrality # 2.3
	from matplotlib import pyplot as plt        # 2.4
	import sva_gm                               # 3.1 собственные модули
	import sva_gm as sgm                        # 3.2
	from sva_gm import shortest_distance        # 3.3
	from sva_gm import shortest_path as pth     # 3.4
	```
2. Явно указываем функции/классы для экспорта:
	```python
	__all__ = [
		'shortest_path',
		'shortest_distance'
	]
	```
3. Разделяем простыню кода на ответственные зоны и выносим их в отдельные функции.
	```python
	# было
	def some_action_with_dataframe(file_input_path: str, file_output_path: str) -> int:
		df = pd.read_excel(file_path, dtype='str')
		df.to_csv(file_output_path, sep=';', encoding='utf-8', index=False)
		return {
            'rows_count': len(df),
            'columns_count': len(df.columns),
            'columns': df.columns
        }


	# стало
    @dataclass
    class DataFrameInfo:
        rows_count: int
        columns_count: int
        columns: list[str]


	def dataframe_from_excel(file_path: str) -> pd.DataFrame:
		return pd.read_excel(file_path, dtype='str')


	def get_dataframe_info(df: pd.DataFrame) -> dict:
		return DataFrameInfo(
            rows_count = len(df),
            columns_count = len(df.columns),
            columns = list(df.columns)
        )


	def dataframe_to_csv(df: pd.DataFrame, file_path: str) -> None:
		df.to_csv(file_path, sep=';', encoding='utf-8', index=False)
	```
4. Используемые только в данном модуле функции отмечаем как приватные с помощью нижнего подчеркивания:
	```python
	def _dijkstra(graph, start_node, tartget_node):
		...
		return shotrest_path, shortest_distance


	def shortest_path(graph, start_node, target_node):
		try:
			return _dijkstra(graph, start_node, tartget_node)[0]
		except KeyError:
			raise ShortestPathNotFoundException()
	```
5. В функциях явно указываем типы данных:
	```python
	def shortest_path(
		graph: Graph,
		start_node: int | float | str,
		target_node: int | float | str,
        parameters: Iterable[str]
	) -> list:
		...
	```
6. Пишем документацию для разработчиков (если нужно объяснить логику работы функции/модуля или пояснить какие аргументы подаются на вход):
	```python
	def _kosaraju(graph: ...) -> ...:
		...


	def _tarjan(graph: ...) -> ...:
		...


	def search_strongly_connected_components(
		graph: Graph,
		algorithm: Callable = _tarjan,
		some_coefficient: float = 0.15
	) -> list[Graph]:
		"""
		Searching strongly connected components in graph.

		Parameters
		----------
		graph     : Graph object.
		algorithm : Function with implementation of the required algorithm.
		            Possible values: _tarjan, _kosaraju.

		Returns
		-------
		List of subgraphs contains strongly connected components.
		"""
		...
	```

# Рекомендации по оптимизации:
1. Возвращайте генераторы вместо итерабельных объектов;
2. Используйте включения списков/словарей/множеств, они быстрее перебора в цикле;
3. Используйте кеширование для функций, результат которых может потребоваться несколько раз.
