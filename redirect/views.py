from django.shortcuts import HttpResponse, redirect
from django.http import HttpResponseRedirect
from urllib.parse import unquote

from .models import RedirectItem, to_from_identifier


def redirect_action(request):
    # 3 to cut off the /R/
    path = unquote(request.get_full_path())[3:]
    # Apache makes this /r/ at the end replacing the last 3 characters
    # for some reason. So we cut off the last three characters. We
    # need to do the same when saving urls
    path = path[:-3]

    from_identifier = to_from_identifier(path)
    matches = RedirectItem.objects.filter(from_identifier=from_identifier)
    if matches.count() > 0:
        m = matches.first()
        m.visits += 1
        return redirect(matches.first().to_url)
    else:
        return HttpResponse(
            f'Redirect url not found:</br>{from_identifier}')
