from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    def custom_page_range(self, a, b):
        return range(int(a), int(b))


def page_range_check(page, max_page):
    if (page-5) < 1:
        page_start = 1
    else:
        page_start = page-5

    for i in range(5):
        if (page+i) > max_page:
            page_end = max_page+1
            break
        else:
            page_end = page+i

    return page_start, page_end