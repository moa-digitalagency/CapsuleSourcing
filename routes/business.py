from flask import render_template
from routes import business_bp
from services.content_service import get_page_content
import logging

logger = logging.getLogger(__name__)


@business_bp.route('/services')
def services():
    try:
        from models.database import Service, ContactInfo
        
        services_list = Service.query.order_by(Service.order).all()
        contact_info = ContactInfo.query.first()
        content = get_page_content('services')
        
        return render_template('services.html', 
            services=services_list, 
            contact_info=contact_info,
            content=content
        )
    except Exception as e:
        logger.error(f"Error in services route: {e}")
        return render_template('errors/500.html'), 500


@business_bp.route('/partenariats')
def partenariats():
    try:
        from models.database import PartnershipType, ContactInfo
        
        partnership_types = PartnershipType.query.order_by(PartnershipType.order).all()
        contact_info = ContactInfo.query.first()
        content = get_page_content('partenariats')
        
        return render_template('partenariats.html', 
            partnership_types=partnership_types,
            contact_info=contact_info,
            content=content
        )
    except Exception as e:
        logger.error(f"Error in partenariats route: {e}")
        return render_template('errors/500.html'), 500


@business_bp.route('/processus')
def processus():
    try:
        from models.database import ProcessStep, ContactInfo
        
        steps = ProcessStep.query.order_by(ProcessStep.order).all()
        contact_info = ContactInfo.query.first()
        content = get_page_content('processus')
        
        return render_template('processus.html', 
            steps=steps,
            contact_info=contact_info,
            content=content
        )
    except Exception as e:
        logger.error(f"Error in processus route: {e}")
        return render_template('errors/500.html'), 500


@business_bp.route('/faq')
def faq():
    try:
        from models.database import FAQ, ContactInfo
        
        faqs = FAQ.query.order_by(FAQ.order).all()
        contact_info = ContactInfo.query.first()
        content = get_page_content('faq')
        
        return render_template('faq.html', 
            faqs=faqs,
            contact_info=contact_info,
            content=content
        )
    except Exception as e:
        logger.error(f"Error in faq route: {e}")
        return render_template('errors/500.html'), 500
