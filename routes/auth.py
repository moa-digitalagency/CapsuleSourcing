from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from app import db
import logging

logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        
        if request.method == 'POST':
            from models.database import User
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
            remember = bool(request.form.get('remember'))
            
            user = User.query.filter(
                (User.username == username) | (User.email == username)
            ).first()
            
            if user and user.check_password(password):
                login_user(user, remember=remember)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                if user.is_admin:
                    return redirect(url_for('admin.dashboard'))
                return redirect(url_for('main.index'))
            
            flash('Identifiants incorrects', 'error')
        
        return render_template('auth/login.html')
    except Exception as e:
        logger.error(f"Error in login route: {e}")
        import traceback
        logger.error(traceback.format_exc())
        db.session.rollback()
        return render_template('errors/500.html'), 500


@auth_bp.route('/register')
def register():
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
@login_required
def logout():
    try:
        logout_user()
        flash('Vous avez ete deconnecte', 'success')
        return redirect(url_for('main.index'))
    except Exception as e:
        logger.error(f"Error in logout route: {e}")
        return redirect(url_for('main.index'))
