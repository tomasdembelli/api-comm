from requests import Request, Session


class ApiComm:
    """HTTP Client"""

    def __init__(self, base_url, token=None, token_type=None, headers=None):
        """Prepare the client."""
        self.session = Session()
        if headers is not None:
            self.session.headers.update(headers)
        self.base_url = base_url.strip('/')
        if token is not None:
            if token_type is None:
                raise ValueError('Token type is required.')
            self.session.headers.update({"Authorization": f'{token_type} {token}'})
        if token_type is not None:
            if token is None:
                raise ValueError('Token is required.')

        post_req = Request('POST', base_url)
        self.prep_post = self.session.prepare_request(post_req)

    def connect(self, method, path=None, headers=None, params=None, data=None):
        """Make HTTP GET request."""
        if path is not None:
            url = '/'.join((self.base_url, path.strip('/')))
        else:
            url = self.base_url
        if method.lower() == 'get':
            return self.session.get(url, headers=headers, params=params)
        elif method.lower() == 'post':
            return self.session.post(url, data=data, headers=headers, params=params)
        elif method.lower() == 'put':
            return self.session.put(url, data=data, headers=headers, params=params)
        elif method.lower() == 'patch':
            return self.session.patch(url, data=data, headers=headers, params=params)
        elif method.lower() == 'delete':
            return self.session.delete(url, headers=headers, params=params)
        else:
            raise ValueError(f'Unsupported HTTP method provided: {method}.')


