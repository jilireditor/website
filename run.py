# Hack to play nicely with Unicode content
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('jilir', 'templates'))

from jilir_data import volumes


def render_page(filename, output_filename, data={}):
    template = env.get_template(filename)
    content = template.render(data)

    f = open(output_filename, 'w')
    f.write(content.encode('utf8'))
    f.close()


if __name__ == "__main__":
    render_page('index.jinja', 'jilir/index.html', {
            'index': True
        })

    render_page('submissions.jinja', 'jilir/submissions.html')

    render_page('issues.jinja', 'jilir/issues.html', {
            'volumes': volumes
        })

    render_page('announcements.jinja', 'jilir/announcements.html')

    render_page('team.jinja', 'jilir/team.html')

    render_page('about.jinja', 'jilir/about.html')
