import re

import httpretty
from mock import patch

from examples import config_examples as conf_ex
from examples import request_examples as req_ex
from examples import response_examples as resp_ex
from leexportpy.lerestresponse import LeRestResponse
from leexportpy.services.hosted_graphite_service import HostedGraphiteService


def test_convert_to_hostedgraphite_data():
    full_ts_resp_object = LeRestResponse(
        {"logs": resp_ex.LOGS, "statistics": resp_ex.TIMESERIES_STATISTICS, "leql": resp_ex.LEQL})
    hosted_graphite_job = HostedGraphiteService(full_ts_resp_object, req_ex.SERVICE_API_KEY,
                                                conf_ex.SEARCH_HOSTED_GRAPHITE)

    hg_data = hosted_graphite_job.transform()
    pattern = re.compile("(\w+\s\d+\.\d+\s\d+\\n)+")

    assert pattern.match(hg_data)


def test_process():
    with patch.object(HostedGraphiteService, 'push', return_value=None) as mock_push:
        hosted_graphite_job = HostedGraphiteService(LeRestResponse(resp_ex.FULL_TIMESERIES_RESP), req_ex.SERVICE_API_KEY,
                                                    conf_ex.SEARCH_HOSTED_GRAPHITE)

        hosted_graphite_job.process()

        assert mock_push.called


@httpretty.activate
def test_push():
    hosted_graphite_job = HostedGraphiteService(LeRestResponse(resp_ex.FULL_TIMESERIES_RESP), req_ex.SERVICE_API_KEY,
                                                conf_ex.SEARCH_HOSTED_GRAPHITE)
    httpretty.register_uri(httpretty.PUT, req_ex.DEST_URL,
                           body="OK")

    hosted_graphite_job.push("payload")

    assert httpretty.has_request()
