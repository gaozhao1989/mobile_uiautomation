import os, logging

current_path = os.getcwd()
workspace_name = 'mobile_uiautomation'
workspace_path = current_path[:current_path.index(workspace_name) + len(workspace_name)]

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('Utils')


class Runner(object):
    def __init__(self, *args):
        if args[0] == '' or args[0] == 'tests':
            self.test_scope = 'tests'
        else:
            self.test_scope = args[0]

    def run_test(self):
        self.generate_results()
        self.generate_html_report()

    def generate_results(self, pytest_scope=workspace_path + '\\tests', results_dir=workspace_path + '\\report'):
        import pytest
        pytest.main([pytest_scope, '--alluredir=' + results_dir])

    def generate_html_report(self, results_dir=workspace_path + '\\report',
                             html_report_dir=workspace_path + '\\report\\html'):
        cmd = 'allure generate ' + results_dir + ' -o ' + html_report_dir
        log.debug(cmd)
        os.system(cmd)


def runner():
    run = Runner('tests')
    run.run_test()


if __name__ == '__main__':
    runner()
