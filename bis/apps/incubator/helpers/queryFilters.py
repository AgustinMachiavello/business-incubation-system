""" Dynamic filtering helpers """


def orderQueryset(queryset, field):
    return queryset.order_by(field)

def filterByCreationDate(queryset, createdFrom, createdTo):
    if (createdFrom and createdTo):
        return queryset.filter(created_at__gte=createdFrom, created_at__lte=createdTo)
    elif (createdFrom and (not createdTo)):
        return queryset.filter(created_at__gte=createdFrom)
    elif (createdTo and (not createdFrom)):
        return queryset.filter(created_at__lte=createdTo)
    else:
        return queryset

def dynamicQuerysetFilter(queryset, fieldsDict=None, createdFrom=None, createdTo=None, orderBy=None):
    if fieldsDict:
        queryset = queryset.filter(**fieldsDict)
    if (createdFrom or createdTo):
        queryset = filterByCreationDate(queryset, createdFrom, createdTo)
    if orderBy:
        queryset = orderQueryset(queryset)
    return queryset
