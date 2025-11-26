"""Service for managing all page content from database."""
from models.database import PageContent, SiteSettings
from app import db


def get_content(page, section, key, default=''):
    """Get a single content value from database."""
    content = PageContent.query.filter_by(page=page, section=section, key=key).first()
    return content.value if content and content.value else default


def get_section_content(page, section):
    """Get all content for a section as a dictionary."""
    contents = PageContent.query.filter_by(page=page, section=section).all()
    return {c.key: c.value for c in contents}


def get_page_content(page):
    """Get all content for a page grouped by section."""
    contents = PageContent.query.filter_by(page=page).all()
    result = {}
    for c in contents:
        if c.section not in result:
            result[c.section] = {}
        result[c.section][c.key] = c.value
    return result


def set_content(page, section, key, value):
    """Set a content value in database."""
    content = PageContent.query.filter_by(page=page, section=section, key=key).first()
    if content:
        content.value = value
    else:
        content = PageContent(page=page, section=section, key=key, value=value)
        db.session.add(content)
    db.session.commit()
    return content


def set_multiple_content(page, section, data_dict):
    """Set multiple content values at once."""
    for key, value in data_dict.items():
        content = PageContent.query.filter_by(page=page, section=section, key=key).first()
        if content:
            content.value = value
        else:
            content = PageContent(page=page, section=section, key=key, value=value)
            db.session.add(content)
    db.session.commit()


def get_setting(key, default=''):
    """Get a site setting value."""
    setting = SiteSettings.query.filter_by(key=key).first()
    return setting.value if setting and setting.value else default


def set_setting(key, value, category='general'):
    """Set a site setting value."""
    setting = SiteSettings.query.filter_by(key=key).first()
    if setting:
        setting.value = value
    else:
        setting = SiteSettings(key=key, value=value, category=category)
        db.session.add(setting)
    db.session.commit()
    return setting


def init_content_if_empty(page, section, key, default_value):
    """Initialize content only if it doesn't exist."""
    content = PageContent.query.filter_by(page=page, section=section, key=key).first()
    if not content:
        content = PageContent(page=page, section=section, key=key, value=default_value)
        db.session.add(content)
        db.session.commit()
    return content
