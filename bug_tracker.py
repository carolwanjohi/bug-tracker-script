from api_requests import get_projects, get_unscheduled_bug_cards
from utils import map_key_values, filter_bugs_states

if __name__ == '__main__':
    projects_found = get_projects()
    
    project_ids = map_key_values(projects_found, 'id')
    
    bugs_found = get_unscheduled_bug_cards(project_ids)

    unstarted_bugs_states = ['unscheduled', 'unstarted', 'planned', 'rejected']

    unstarted_bugs = filter_bugs_states(bugs_found, unstarted_bugs_states)

    inporgess_bugs_states = ['started', 'finished']

    inporgess_bugs = filter_bugs_states(bugs_found, inporgess_bugs_states)

    done_bugs_states = ['delivered', 'accepted']

    done_bugs = filter_bugs_states(bugs_found, done_bugs_states)
