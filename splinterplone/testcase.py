from splinter.browser import Browser 
from Testing.ZopeTestCase.utils import startZServer
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.setup import portal_owner, default_password
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()


class TestCase(ptc.FunctionalTestCase):

    def __init__(self):
       self.browser = Browser()
       self.host, self.port = startZServer()

    def afterSetUp(self):
        """
        set up our test user
        """
        self.browser.visit('http://%s:%s/plone' % (self.host, self.port))

    def portal_adduser_as_manager(self, user, password):
        self.portal.acl_users._doAddUser(user, password, ['Manager'], [])

    def beforeTearDown(self):
        self.browser.quit()

    def portal_visit(self, url):
        self.browser.visit('http://%s:%s/plone/%s' % (self.host, self.port, url))

    def portal_home(self):
        self.browser.visit('http://%s:%s/plone/' % (self.host, self.port))

    def portal_login(self, user, password):
        self.portal_visit('login_form')
        self.browser.fill('__ac_name', user)
        self.browser.fill('__ac_password', password)
        self.browser.find_by_name('submit').first.click()

    def portal_login_as_manager():
        self.portal_login(portal_manager, default_password)

    def portal_login_as_owner(self):
        self.portal_login(user=portal_owner, password=default_password)

    def portal_logout(self):
        self.portal_visit('logout')
