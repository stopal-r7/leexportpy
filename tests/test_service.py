import pytest

from leexportpy.service import Service


def test_process():
    with pytest.raises(NotImplementedError):
        service_ojb = Service("test_data", "test_api_key", {})
        service_ojb.process()


def test_transform():
    with pytest.raises(NotImplementedError):
        service_ojb = Service("test_data", "test_api_key", {})
        service_ojb._transform()


def test_push():
    service_obj = Service("test_data", "test_api_key", {})
    result = service_obj._push("payload")
    assert result is True

    result = service_obj._push(None)
    assert result is False
