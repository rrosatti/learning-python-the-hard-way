from nose.tools import *
import re

def assert_response(resp, contains=None, macthes=None, headers=None, status="200"):
	
	assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)

	if status == "200":
		assert resp.data, "Response data is empty."

	if contains:
		assert contains in resp.data, "REsponse does not contain %r" % contains

	if macthes:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "Response does not match %r" % matches

	if headers:
		assert_equal(resp.headers, headers)
	