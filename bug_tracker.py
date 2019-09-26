from api_requests import get_projects, get_unscheduled_bug_cards, post_to_bug_tracker_channel
from utils import map_key_values, filter_bugs_states

if __name__ == '__main__':
    projects_found = get_projects()
    
    project_ids = map_key_values(projects_found, 'id')
    
    bugs_found = get_unscheduled_bug_cards(project_ids)

    unstarted_bugs_states = ['unscheduled', 'unstarted', 'planned', 'rejected']

    unstarted_bugs = filter_bugs_states(bugs_found, unstarted_bugs_states)

    inporgess_bugs_states = ['started', 'finished']

    inporgess_bugs = filter_bugs_states(bugs_found, inporgess_bugs_states)

    post_to_bug_tracker_channel(inporgess_bugs, '*Inprogress*')

    done_bugs_states = ['delivered', 'accepted']

    done_bugs = filter_bugs_states(bugs_found, done_bugs_states)
