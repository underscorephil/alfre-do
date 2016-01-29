
import sys
import re
from workflow import Workflow, ICON_WEB, ICON_WARNING
import argparse


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?')
    parser.add_argument('--default-list', dest='default_list', nargs='?')
    args = parser.parse_args(wf.args)

    # save default list if passed in
    if args.default_list:
        wf.settings['default_list'] = args.default_list
        return 0

    # get query from alfred
    query = args.query

    # get a set of tags and remove them from the task title
    tags = {tag.strip("#") for tag in query.split() if tag.startswith("#")}
    task_title = re.sub(r"(?:\#|:)[A-Za-z]+", "", query).strip()

    # look for a specified list
    twodo_list = re.search('\s:[A-Z][a-z]+$', query)
    if twodo_list:
        twodo_list = twodo_list.group(0).replace(':', '').strip()

    # check for a default list
    if not twodo_list:
        default_list = wf.settings.get('default_list', None)
        if not default_list:
            wf.add_item('No Default List Set.',
                        'Please use twodo default list to set the default list',
                        valid=False,
                        icon=ICON_WARNING)
            wf.send_feedback()
            return 0
        else:
            twodo_list = default_list

    # structure twodo "api" call
    url = 'twodo://x-callback-url/add?task=%s&forlist=%s' % (task_title, twodo_list)

    # Send the results to Alfred as XML
    alfred_title = 'Add task: %s' % (task_title)
    alfred_subtitle = 'List: %s' % (twodo_list)
    # if we have tags...add them!
    if len(tags):
        alfred_tags = ",".join(tags)
        url += '&tags=%s' % (alfred_tags)
        alfred_subtitle += ' Tags: %s' % (alfred_tags)
    wf.add_item(title=alfred_title, subtitle=alfred_subtitle,
                arg=url, valid=True)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
