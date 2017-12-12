import glitch.api.Connector as Connector


def get_package_list():
    Connector.post_request("/Store/GetPackages")
