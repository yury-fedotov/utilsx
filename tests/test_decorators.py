from utilsx import return_element


class TestReturnElement:
    def test_no_args_two_returns(self) -> None:
        _default_return_value = (1, "la")

        def _example_function() -> tuple[int, str]:
            return _default_return_value

        getter_of_first = return_element(0)(_example_function)
        getter_of_second = return_element(1)(_example_function)
        assert getter_of_first() == _default_return_value[0]
        assert getter_of_second() == _default_return_value[1]
