import psycopg2
import os

def test_connection(connection_string):
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Connection successful! PostgreSQL version: {version[0]}")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

# Test both connection strings
print("Testing database connections...")

print("\n1. Testing connection WITHOUT c-2 subdomain:")
test_connection("postgresql://neondb_owner:npg_jZXHKdP8UL5f@ep-little-pine-ada2gu0j-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require")

print("\n2. Testing connection WITH c-2 subdomain:")
test_connection("postgresql://neondb_owner:npg_jZXHKdP8UL5f@ep-little-pine-ada2gu0j-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require")

print("\n3. Testing connection WITH c-2 and channel_binding:")
test_connection("postgresql://neondb_owner:npg_jZXHKdP8UL5f@ep-little-pine-ada2gu0j-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
