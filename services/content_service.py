"""Service for managing all page content from database."""
import logging
from app import db

logger = logging.getLogger(__name__)


def get_content(page, section, key, default=''):
    """Get a single content value from database."""
    try:
        from models.database import PageContent
        content = PageContent.query.filter_by(page=page, section=section, key=key).first()
        return content.value if content and content.value else default
    except Exception as e:
        logger.warning(f"Error getting content: {e}")
        return default


def get_section_content(page, section):
    """Get all content for a section as a dictionary."""
    try:
        from models.database import PageContent
        contents = PageContent.query.filter_by(page=page, section=section).all()
        return {c.key: c.value for c in contents}
    except Exception as e:
        logger.warning(f"Error getting section content: {e}")
        return {}


def get_page_content(page):
    """Get all content for a page grouped by section."""
    try:
        from models.database import PageContent
        contents = PageContent.query.filter_by(page=page).all()
        result = {}
        for c in contents:
            if c.section not in result:
                result[c.section] = {}
            result[c.section][c.key] = c.value
        return result
    except Exception as e:
        logger.warning(f"Error getting page content: {e}")
        return {}


def set_content(page, section, key, value):
    """Set a content value in database."""
    try:
        from models.database import PageContent
        content = PageContent.query.filter_by(page=page, section=section, key=key).first()
        if content:
            content.value = value
        else:
            content = PageContent(page=page, section=section, key=key, value=value)
            db.session.add(content)
        db.session.commit()
        return content
    except Exception as e:
        logger.error(f"Error setting content: {e}")
        db.session.rollback()
        return None


def set_multiple_content(page, section, data_dict):
    """Set multiple content values at once."""
    try:
        from models.database import PageContent
        for key, value in data_dict.items():
            content = PageContent.query.filter_by(page=page, section=section, key=key).first()
            if content:
                content.value = value
            else:
                content = PageContent(page=page, section=section, key=key, value=value)
                db.session.add(content)
        db.session.commit()
    except Exception as e:
        logger.error(f"Error setting multiple content: {e}")
        db.session.rollback()


def get_setting(key, default=''):
    """Get a site setting value."""
    try:
        from models.database import SiteSettings
        setting = SiteSettings.query.filter_by(key=key).first()
        return setting.value if setting and setting.value else default
    except Exception as e:
        logger.warning(f"Error getting setting: {e}")
        return default


def set_setting(key, value, category='general'):
    """Set a site setting value."""
    try:
        from models.database import SiteSettings
        setting = SiteSettings.query.filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            setting = SiteSettings(key=key, value=value, category=category)
            db.session.add(setting)
        db.session.commit()
        return setting
    except Exception as e:
        logger.error(f"Error setting setting: {e}")
        db.session.rollback()
        return None


def init_content_if_empty(page, section, key, default_value):
    """Initialize content only if it doesn't exist."""
    try:
        from models.database import PageContent
        content = PageContent.query.filter_by(page=page, section=section, key=key).first()
        if not content:
            content = PageContent(page=page, section=section, key=key, value=default_value)
            db.session.add(content)
            db.session.commit()
        return content
    except Exception as e:
        logger.error(f"Error initializing content: {e}")
        db.session.rollback()
        return None
