import os, yaml

current_path = os.getcwd()
workspace_name = 'mobile_uiautomation'
workspace_path = current_path[:current_path.index(workspace_name) + len(workspace_name)]


def get_yaml_data(file_path):
    stream = open(file_path, 'r', encoding='utf-8')
    yaml_data = yaml.load(stream)
    stream.close()
    return yaml_data


def get_android_caps():
    android_caps = get_yaml_data(workspace_path + '\\config\\android.yaml')['capabilities']
    app_rel_path = android_caps['app']
    android_caps['app'] = get_app_rel_path(app_rel_path)
    return android_caps


def get_ios_caps():
    ios_caps = get_yaml_data(workspace_path + '\\config\\ios.yaml')['capabilities']
    app_rel_path = ios_caps['app']
    ios_caps['app'] = get_app_rel_path(app_rel_path)
    return ios_caps


def get_appium_config():
    return get_yaml_data(workspace_path + '\\config\\server.yaml')['appium']


def get_test_platform():
    return get_yaml_data(workspace_path + '\\config\\server.yaml')['platform']


def get_page_locators(locator_file):
    return get_yaml_data(workspace_path + '\\pages\\locator\\' + locator_file + '.yaml')


def get_locator_properties(locator_file, locator_name, test_platform):
    yaml_data = get_page_locators(locator_file)
    return yaml_data[locator_file]['elements'][locator_name][test_platform]['find_by'], \
           yaml_data[locator_file]['elements'][locator_name][test_platform]['value']


def get_app_rel_path(app_name):
    return os.path.join(workspace_path, 'apps', app_name)
