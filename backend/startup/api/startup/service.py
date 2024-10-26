from ...models import Startup, Founder, Batch, Category
from django.db.models import Count, Q

def filter_startups(queryset,
    categories_names=None, 
    batch_name=None,
    phase=None,
    status=None,
    priority=None
):
    if categories_names: 
        queryset = queryset.filter(categories__name__in=categories_names) \
                           .annotate(num_categories=Count('categories', filter=Q(categories__name__in=categories_names))) \
                           .filter(num_categories=len(categories_names))
        
    if batch_name:
        queryset = queryset.filter(batch__name=batch_name)

    if phase:
        queryset = queryset.filter(phase=phase)

    if status:
        queryset = queryset.filter(status=status)

    if priority:
        queryset = queryset.filter(priority=priority)

    return queryset

