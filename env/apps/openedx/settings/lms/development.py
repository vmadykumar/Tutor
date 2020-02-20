# -*- coding: utf-8 -*-
import os
from lms.envs.devstack import *

####### Settings common to LMS and CMS

DEFAULT_FROM_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
SERVER_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
TECH_SUPPORT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
CONTACT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
BUGS_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
UNIVERSITY_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
PRESS_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
BULK_EMAIL_DEFAULT_FROM_EMAIL = "no-reply@" + ENV_TOKENS["LMS_BASE"]
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
API_ACCESS_FROM_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]

# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]

EMAIL_USE_SSL = False

LOCALE_PATHS.append("/openedx/locale")


######## End of settings common to LMS and CMS

######## Common LMS settings

# Fix media files paths
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
PROFILE_IMAGE_BACKEND["options"]["location"] = os.path.join(
    MEDIA_ROOT, "profile-images/"
)

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

COURSE_CATALOG_VISIBILITY_PERMISSION = "see_in_catalog"
COURSE_ABOUT_VISIBILITY_PERMISSION = "see_about_page"

# JWT is authentication for other openedx services
JWT_AUTH["JWT_ISSUER"] = "http://uat-lms.pratian.com/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "ikoBijnDSRftgurcByizW0zJ"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = None

# Allow insecure oauth2 for local interaction with local containers
OAUTH_ENFORCE_SECURE = False

# Create folders if necessary
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE, ORA2_FILEUPLOAD_ROOT]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common LMS settings

OAUTH_OIDC_ISSUER = "http://uat-lms.pratian.com/oauth2"

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

