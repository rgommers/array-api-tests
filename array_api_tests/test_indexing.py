"""
https://data-apis.github.io/array-api/latest/API_specification/indexing.html
"""

from hypothesis import given
from hypothesis.strategies import shared

from .hypothesis_helpers import slices, sizes
from ._array_module import arange

@given(shared(sizes, key='array_sizes'), slices(shared(sizes, key='array_sizes')))
def test_slicing(size, s):
    # Test that slices on arrays give the same result as Python lists.

    # Sanity check that the strategies are working properly
    if s.start is not None:
        assert -size <= s.start <= max(0, size - 1)
    if s.stop is not None:
        assert -size <= s.stop <= size

    a = arange(size)
    l = list(range(size))
    sliced_list = l[s]
    sliced_array = a[s]

    assert len(sliced_list) == sliced_array.size
    for i in range(len(sliced_list)):
        assert sliced_list[i] == sliced_array[i]