from django import template

register = template.Library()


def paginator(context, adjacent_pages=2):
    paginator_obj = context['paginator']
    page_obj = context['page_obj']
    page = page_obj.number

    num_pages = paginator_obj.num_pages
    start_page = max(page - adjacent_pages, 1)
    if start_page <= 3:
        start_page = 1
    end_page = page + adjacent_pages + 1
    if end_page >= num_pages - 1:
        end_page = num_pages + 1
    page_numbers = [n for n in range(start_page, end_page) if n > 0 and n <= num_pages]

    request = context['request']
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']

    return {
        'query_string': query_dict.urlencode(),
        'page_obj': page_obj,
        'paginator': paginator_obj,
        'page': page,
        'pages': num_pages,
        'page_numbers': reversed(page_numbers),
        'show_first': 1 not in page_numbers,
        'show_last': num_pages not in page_numbers,
    }

register.inclusion_tag('cards/paginator.html', takes_context=True)(paginator)