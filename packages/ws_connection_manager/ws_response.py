import time

content = (
    """
    <div hx-swap-oob="{ordering}:#{div_id}">
        <p>{time}: {client_id} : {message}</p>
    </div>
    """
)


def ws_response(client_id, message, div_id="content", from_top=False):
    ordering = "afterbegin" if from_top else "beforeend"
    return content.format(time=time.strftime(
        '%X %x %Z'), message=message, client_id=client_id, div_id=div_id, ordering=ordering)
