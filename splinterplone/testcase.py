from splinter.browser import Browser
from Testing.ZopeTestCase.utils import startZServer
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.setup import portal_owner, default_password
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()


class TestCase(ptc.PloneTestCase):

    def __init__(self):
        self.browser = Browser(driver_name='webdriver.firefox')
        self.host, self.port = startZServer()

    def afterSetUp(self):
        self.browser.visit('http://%s:%s/plone' % (self.host, self.port))

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

    def portal_login_as_owner(self):
        self.portal_login(user=portal_owner, password=default_password)

    def portal_logout(self):
        self.portal_visit('logout')

    def portal_search(self, search_word):
        self.browser.fill('SearchableText','%s' % (search_word))
        self.browser.find_by_css('.searchButton').first.click()

    def portal_navigate_submenu(self, option):
        self.browser.find_by_xpath("//li[contains(@id, 'contentview')]/a[text()='%s']" % (option)).first.click()

    def portal_click_a_personaltool(self, personaltool):
        self.browser.click_link_by_href('http://%s:%s/plone/dashboard' % (self.host, self.port))
        self.browser.click_link_by_text('%s' % (personaltool))

    def portal_add_user(self, fullname, username, email, password):
        self.portal_click_a_personaltool('Site Setup')
        self.browser.click_link_by_text('Users and Groups')
        self.browser.find_by_name('form.button.AddUser').first.click()
        self.browser.fill('form.fullname','%s' % (fullname))
        self.browser.fill('form.username','%s' % (username))
        self.browser.fill('form.email','%s' % (email))
        self.browser.fill('form.password','%s' % (password))
        self.browser.fill('form.password_ctl','%s' % (password))
        self.browser.find_by_id('form.actions.register').first.click()

    def portal_add_user_as_manager(self, fullname, username, email, password):
        self.portal_click_a_personaltool('Site Setup')
        self.browser.click_link_by_text('Users and Groups')
        self.browser.find_by_name('form.button.AddUser').first.click()
        self.browser.fill('form.fullname','%s' % (fullname))
        self.browser.fill('form.username','%s' % (username))
        self.browser.fill('form.email','%s' % (email))
        self.browser.fill('form.password','%s' % (password))
        self.browser.fill('form.password_ctl','%s' % (password))
        self.browser.find_by_id('form.groups.0').first.click()
        self.browser.find_by_id('form.actions.register').first.click()

    def portal_change_user_role(self, username, new_role):
        self.portal_click_a_personaltool('Site Setup')
        self.browser.click_link_by_text('Users and Groups')
        self.browser.find_by_xpath("//tr[*/input[@value='%s']]//input[@value='%s']" % (username, new_role)).first.click()
        self.browser.find_by_name('form.button.Modify').first.click()

    def portal_click_enable_content_types(self):
        self.browser.find_by_css('a[title="Add new items inside this item"]').first.click()

    def portal_add_content_type(self, type):
        self.portal_click_enable_content_types()
        self.browser.click_link_by_text('%s' % (type))

    def portal_click_content_item_action(self):
        self.browser.find_by_css('a[title="Actions for the current content item"]').first.click()

    def portal_add_item_action(self, type):
        self.portal_click_content_item_action()
        self.browser.click_link_by_text('%s' % (type))

    def portal_list_states(self):
        self.browser.find_by_css('a[title="Change the state of this item"]').first.click()

    def portal_modify_state_to(self, state):
        self.portal_list_states()
        self.browser.click_link_by_text('%s' % (state))
