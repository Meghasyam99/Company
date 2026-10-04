class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('hi iam middleware')
    def __call__(self, req):
        print('before view')
        response=self.get_response(req)
        print('After view')
        return response