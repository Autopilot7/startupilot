from rest_framework.pagination import BasePagination
from rest_framework.response import Response

class OffsetLimitPagination(BasePagination):
    default_limit = 25  # Default number of items to return
    max_limit = 100  # Maximum limit to prevent overloading

    def paginate_queryset(self, queryset, request, view=None):
        try:
            self.offset = int(request.query_params.get('offset', 0))
            self.limit = int(request.query_params.get('limit', self.default_limit))
        except ValueError:
            self.offset = 0
            self.limit = self.default_limit

        # Ensure the limit is within the allowed range
        self.limit = min(self.limit, self.max_limit)

        self.total = len(queryset)
        return queryset[self.offset:self.offset + self.limit]

    def get_paginated_response(self, data):
        return Response({
            'count': self.total,
            'offset': self.offset,
            'limit': self.limit,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

    def get_next_link(self):
        if self.offset + self.limit >= self.total:
            return None
        return f'?offset={self.offset + self.limit}&limit={self.limit}'

    def get_previous_link(self):
        if self.offset <= 0:
            return None
        return f'?offset={max(self.offset - self.limit, 0)}&limit={self.limit}'
