from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from urllib.parse import urlencode


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    # max_page_size = 5

    def get_paginated_response(self, data):
        next_url = None
        if self.page.has_next():
            params = {
                'page': self.page.next_page_number(),
                self.page_size_query_param: self.get_page_size(self.request),
            }
            next_url = self.request.build_absolute_uri('?' + urlencode(params))

        previous_url = None
        if self.page.has_previous():
            params = {
                'page': self.page.previous_page_number(),
                self.page_size_query_param: self.get_page_size(self.request),
            }
            previous_url = self.request.build_absolute_uri('?' + urlencode(params))

        return Response({
            'count': self.page.paginator.count,
            'next': next_url,
            'previous': previous_url,
            'results': data
        })

