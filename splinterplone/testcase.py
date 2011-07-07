from splinter.browser import Browser 
from Testing.ZopeTestCase.utils import startZServer
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.setup import portal_owner, default_password
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()


class TestCase(ptc.FunctionalTestCase):

    def __init__(self):
       self.browser = Browser(driver_name='webdriver.firefox')
       self.host, self.port = startZServer()

    def afterSetUp(self):
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

    def portal_add_content_type(self, type):
        self.portal_visit('folder_factories')
        folder_url = self.browser.request_url.rstrip('folder_factories')
        self.browser.choose('url', folder_url + 'createObject?type_name=%s' % (type))
        self.browser.find_by_name('form.button.Add').first.click()

    def portal_modify_state_to(self, state):
        self.browser.find_by_id('plone-contentmenu-workflow').first.click()
        self.browser.click_link_by_text('%s' % (state))

    def portal_list_states(self):
        self.browser.find_by_id('plone-contentmenu-workflow').first.click()

    def portal_list_enable_content_types(self):
        pass
