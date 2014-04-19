
import sys
import re
from workflow import Workflow, ICON_WEB, ICON_WARNING
import argparse


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?')
    parser.add_argument('--default-list', dest='default_list', nargs='?')
    args = parser.parse_args(wf.args)

    # get query from alfred
    query = args.query

    tags = {tag.strip("#") for tag in query.split() if tag.startswith("#")}
    task_title = re.sub(r"(?:\#|:)[A-Za-z]+", "", query).strip()

    twodo_list = re.search('\s:[A-Z][a-z]+$', query)
    if twodo_list:
        twodo_list = twodo_list.group(0).replace(':', '').strip()

    # save default list
    if args.default_list:
        wf.settings['default_list'] = args.default_list
        wf.add_item('Set list', 'list', valid=False)
        return 0

    # check for a default list
    if not twodo_list:
        default_list = wf.settings.get('default_list', None)
        if not default_list:
            wf.add_item('No Default List Set.',
                        'Please use defaultlist to set the default list\
                         or specify a list',
                        valid=False,
                        icon=ICON_WARNING)
            wf.send_feedback()
            return 0
        else:
            twodo_list = default_list

    url = 'twodo:///add?task=%s&forlist=%s' % (task_title, twodo_list)
    if len(tags):
        url += '&tags=%s' % (",".join(tags))
    # Send the results to Alfred as XML
    alfred_title = 'Add task: %s' % (task_title)
    wf.add_item(title=alfred_title, arg=url, valid=True)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
