# Vercel Deployment Guide

## 🚀 Deploy Django Finance Portfolio Manager to Vercel

This guide will help you deploy your Django application to Vercel with PostgreSQL database.

## ⚠️ Important Note

**Vercel has limitations for Django apps:**
- Serverless functions have 10-second timeout (Hobby plan) or 60-second (Pro plan)
- SQLite doesn't work on Vercel (use PostgreSQL instead)
- File uploads are ephemeral (files don't persist between deployments)
- Better suited for stateless applications

**Recommended alternatives for full Django apps:**
- **Railway.app** (Best for Django, includes PostgreSQL)
- **Render.com** (Great for Django, free tier available)
- **PythonAnywhere** (Designed for Django/Flask)
- **Heroku** (Classic choice)
- **DigitalOcean App Platform**

## 📋 Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code needs to be in a GitHub repository
3. **PostgreSQL Database**: Get one from:
   - [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres) (Recommended)
   - [Neon.tech](https://neon.tech) (Free tier available)
   - [Railway.app](https://railway.app) (PostgreSQL only)
   - [Supabase](https://supabase.com) (Free tier available)

## 🔧 Step 1: Prepare Your Code

The project is already configured for Vercel with these files:
- ✅ `vercel.json` - Vercel configuration
- ✅ `build_files.sh` - Build script
- ✅ `requirements.txt` - Updated with deployment packages
- ✅ `settings.py` - Updated for production
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Files to ignore

## 📦 Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
cd finance_portfolio
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Django Finance Portfolio"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/finance-portfolio.git
git branch -M main
git push -u origin main
```

## 🗄️ Step 3: Set Up PostgreSQL Database

### Option A: Vercel Postgres (Recommended)

1. Go to your Vercel dashboard
2. Navigate to Storage → Create Database
3. Select "Postgres"
4. Note down the connection string

### Option B: Neon.tech (Free Tier)

1. Sign up at [neon.tech](https://neon.tech)
2. Create a new project
3. Copy the connection string (starts with `postgresql://`)

### Option C: Supabase (Free Tier)

1. Sign up at [supabase.com](https://supabase.com)
2. Create a new project
3. Go to Settings → Database
4. Copy the connection string

## 🚀 Step 4: Deploy to Vercel

### Method 1: Via Vercel Dashboard (Easiest)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Configure project:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as is)
   - **Build Command**: `bash build_files.sh`
   - **Output Directory**: Leave empty

4. **Add Environment Variables** (IMPORTANT!):
   Click "Environment Variables" and add:
   
   ```
   SECRET_KEY=your-super-secret-key-here-generate-a-new-one
   DEBUG=False
   ALLOWED_HOSTS=.vercel.app
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

   **Generate a secure SECRET_KEY:**
   ```python
   # Run this in Python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

5. Click **Deploy**

### Method 2: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Follow the prompts
# Set environment variables when prompted
```

## 🔐 Step 5: Configure Environment Variables

In Vercel Dashboard → Settings → Environment Variables, add:

| Variable | Value | Example |
|----------|-------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-xyz123...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | `.vercel.app` | `.vercel.app` |
| `DATABASE_URL` | PostgreSQL URL | `postgresql://user:pass@host:5432/db` |

**Important:** Make sure all variables are set for **Production** environment!

## 📊 Step 6: Run Database Migrations

After deployment, you need to run migrations on the production database.

### Method A: Using Vercel CLI

```bash
# In your local project directory
vercel env pull .env.production
source .env.production

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Method B: Using Local Migration Script

```bash
# Install psycopg2 locally
pip install psycopg2-binary

# Set DATABASE_URL temporarily
export DATABASE_URL="your-production-database-url"

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Method C: Using Railway/Render for Database Setup

If migrations fail, consider using Railway or Render temporarily:
1. Deploy to Railway/Render
2. Run migrations there
3. Use the same database for Vercel

## ✅ Step 7: Verify Deployment

Visit your Vercel URL: `https://your-app.vercel.app`

Check:
- [ ] Home page loads
- [ ] Can sign up/login
- [ ] Can add transactions
- [ ] Static files load (Tailwind CSS working)
- [ ] Database operations work

## 🐛 Common Issues & Solutions

### Issue 1: "502 Bad Gateway"
**Cause:** Build failed or environment variables missing
**Solution:** 
- Check Vercel build logs
- Verify all environment variables are set
- Check `requirements.txt` has all packages

### Issue 2: Static files not loading
**Cause:** Static files not collected
**Solution:**
```bash
# Ensure build_files.sh runs collectstatic
python manage.py collectstatic --noinput
```

### Issue 3: Database connection errors
**Cause:** Wrong DATABASE_URL or database not accessible
**Solution:**
- Verify DATABASE_URL format: `postgresql://user:password@host:5432/dbname`
- Check database is accessible from Vercel
- Ensure database allows external connections

### Issue 4: "Function timeout"
**Cause:** Vercel serverless timeout (10s hobby, 60s pro)
**Solution:**
- Optimize database queries
- Add indexes to models
- Consider upgrading to Pro plan
- Or use Railway/Render instead

### Issue 5: Migrations not applied
**Cause:** Migrations need to be run manually
**Solution:** Follow Step 6 above

### Issue 6: CSRF verification failed
**Cause:** CSRF_TRUSTED_ORIGINS not set
**Solution:** Add your Vercel domain to settings.py:
```python
CSRF_TRUSTED_ORIGINS = ['https://your-app.vercel.app']
```

## 🎯 Alternative: Deploy to Railway (Recommended for Django)

Railway is better suited for Django apps:

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add PostgreSQL
railway add

# Deploy
railway up

# Run migrations
railway run python manage.py migrate

# Create superuser
railway run python manage.py createsuperuser
```

Railway provides:
- ✅ PostgreSQL database included
- ✅ No timeout issues
- ✅ Easier migrations
- ✅ Better for Django
- ✅ Free tier available

## 🎯 Alternative: Deploy to Render

Render is also excellent for Django:

1. Go to [render.com](https://render.com)
2. Connect GitHub repo
3. Select "Web Service"
4. Configure:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn finance_portfolio.wsgi:application`
5. Add PostgreSQL database
6. Set environment variables
7. Deploy!

## 📚 Additional Resources

- [Vercel Python Docs](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Railway Django Guide](https://docs.railway.app/guides/django)
- [Render Django Guide](https://render.com/docs/deploy-django)

## 🔒 Security Checklist

Before going live:
- [ ] Change SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS (Vercel does this automatically)
- [ ] Set secure cookie settings
- [ ] Review Django security checklist

## 💡 Tips

1. **Use Railway or Render** for better Django support
2. **Monitor your logs** in Vercel dashboard
3. **Set up backups** for your database
4. **Use environment variables** for all secrets
5. **Test locally** with PostgreSQL before deploying
6. **Keep requirements.txt** updated

## 🆘 Need Help?

If deployment fails:
1. Check Vercel build logs
2. Verify environment variables
3. Test locally with same configuration
4. Consider using Railway/Render instead
5. Check database connectivity

---

**Note:** While Vercel can host Django apps, it's optimized for Next.js and serverless functions. For production Django apps, consider **Railway**, **Render**, or **PythonAnywhere** for a better experience.
