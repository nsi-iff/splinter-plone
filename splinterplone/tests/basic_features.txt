======================
Basic Features of Splinter-Plone
======================
   Login with the owner role
   >>> self.portal_login_as_owner()
   >>> self.browser.is_text_present('You are now logged in')
   True

   Logout in portal
   >>> self.portal_logout()
   >>> self.browser.is_text_present('You are now logged out')
   True
   
   Create user manager and login
   >>> self.portal_adduser_as_manager('manager','manager')
   >>> self.portal_login('manager','manager')
   >>> self.portal_logout()

   Visit portal home
   >>> self.portal_home()

   Visit any page in portal, for example search page
   >>> self.portal_visit('search')
