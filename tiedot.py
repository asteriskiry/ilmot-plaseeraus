from.models import Participant
def jarjestely(uid)
    for i in Participant.objects.filter(event_type=uid)

def jarjestely2(uid):
    lista=Participant.objects.filter(event_type=uid)

