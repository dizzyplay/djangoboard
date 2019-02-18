from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    def custom_page_range(self, start, end):
        return range(int(start), int(end))


def page_range_check(page, max_page, page_interval=5):
    # page_interval 은 선택된 페이지 번호 포함한 개수
    if (page - page_interval) < 1:
        page_start = 1
    else:
        page_start = page - (page_interval-1)

    for i in range(page_interval+1):
        if (page + i) > max_page:
            page_end = max_page + 1
            break
        else:
            page_end = page + i

    return page_start, page_end



