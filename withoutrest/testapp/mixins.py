from django.http import HttpResponse
class HttpResponseMixins(object):
    def render_to_http_response(self,json_data):
        return HttpResponse(json_data,content_type='application/json')
