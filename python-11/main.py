from api.models import User, Agent, Event, Group
import datetime

def get_active_users():
    # Traga todos os uarios ativos, seu último login deve ser menor que 10 dias.
    today_less_ten = datetime.date.today() - datetime.timedelta(10)
    queryset = User.objects.filter(last_login__gte=today_less_ten)
    return queryset


def get_amount_users():
    #  Retorne a quantidade total de usuarios do sistema
    queryset = User.objects.count()
    return queryset


def get_admin_users():
    #  Traga todos os usuarios com grupo = 'admin
    queryset = User.objects.filter(group__name='admin')
    return queryset


def get_all_debug_events():
    #  Traga todos os eventos com tipo debug
    queryset = Event.objects.filter(level='debug')
    return queryset


def get_all_critical_events_by_user(agent):
    #  Traga todos os eventos do tipo critico de um usuário específico
    queryset = Event.objects.filter(level='critical', agent=agent)
    return queryset


def get_all_agents_by_user(username):
    #  Traga todos os agentes de associados a um usuário pelo nome do usuário
    queryset = Agent.objects.filter(user__name=username)
    return queryset


def get_all_events_by_group():
    #  Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information
    queryset = Group.objects.filter(user__agent__event__level='information')
    return queryset