def get_pagination_text(page: int, max_page: int, params_encoded: str = '') -> str:
    '''
    <li class="active pink lighten-2"><a href="#!">1</a></li>
    <li class="waves-effect"><a href="#!">2</a></li>
    <li class="disabled"><a href="#!"><i>...</i></a></li>
    '''
    page_list = []
    if max_page <= 9:
        page_list = list(range(1, max_page + 1))
    elif page <= 4:
        for i in range(1, page + 3):
            page_list.append(i)
        page_list.append('...')
        page_list.append(max_page)
    elif max_page - page <= 3:
        page_list.append(1)
        page_list.append('...')
        for i in range(page - 2, max_page + 1):
            page_list.append(i)
    else:
        page_list.append(1)
        page_list.append('...')
        for i in range(page - 2, page + 3):
            page_list.append(i)
        page_list.append('...')
        page_list.append(max_page)

    ret = ''
    for p in page_list:
        if p == '...':
            ret += '<li class="disabled"><a href="#!"><i>...</i></a></li>'
        elif p == page:
            ret += f'<li class="active pink lighten-2"><a href="#!">{p}</a></li>'
        else:
            if params_encoded:
                ret += f'<li class="waves-effect"><a href="?{params_encoded}&page={p}">{p}</a></li>'
            else:
                ret += f'<li class="waves-effect"><a href="?page={p}">{p}</a></li>'
    return ret
