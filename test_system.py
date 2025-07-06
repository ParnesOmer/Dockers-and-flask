#!/usr/bin/env python3
"""
Simple Test Script for Multi-Language Code Execution System
This script tests all services to ensure they are working correctly.
"""

import requests
import time
import json
import sys

# Configuration
ROUTER_URL = "http://localhost:5000"
CLIENT_URL = "http://localhost:5004"
TIMEOUT = 10

def test_health_endpoints():
    """Test health endpoints of all services"""
    print("🔍 Testing Health Endpoints...")
    
    services = {
        'router': f"{ROUTER_URL}/health",
        'python-executor': f"{ROUTER_URL.replace(':5000', ':5001')}/health",
        'java-executor': f"{ROUTER_URL.replace(':5000', ':5002')}/health",
        'dart-executor': f"{ROUTER_URL.replace(':5000', ':5003')}/health"
    }
    
    all_healthy = True
    
    for service_name, url in services.items():
        try:
            response = requests.get(url, timeout=TIMEOUT)
            if response.status_code == 200:
                print(f"  ✅ {service_name}: Healthy")
            else:
                print(f"  ❌ {service_name}: Unhealthy (Status: {response.status_code})")
                all_healthy = False
        except Exception as e:
            print(f"  ❌ {service_name}: Unreachable ({str(e)})")
            all_healthy = False
    
    return all_healthy

def test_code_execution():
    """Test code execution for each language"""
    print("\n🚀 Testing Code Execution...")
    
    test_codes = {
        'python': 'print("Hello from Python!")',
        'java': 'public class Main { public static void main(String[] args) { System.out.println("Hello from Java!"); } }',
        'dart': 'void main() { print("Hello from Dart!"); }'
    }
    
    all_successful = True
    
    for language, code in test_codes.items():
        try:
            print(f"  Testing {language}...")
            response = requests.post(
                f"{ROUTER_URL}/execute",
                json={'code': code},
                timeout=TIMEOUT
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"    ✅ {language}: Success")
                if 'Code output' in result:
                    print(f"      Output: {result['Code output'].strip()}")
            else:
                print(f"    ❌ {language}: Failed (Status: {response.status_code})")
                print(f"      Error: {response.text}")
                all_successful = False
                
        except Exception as e:
            print(f"    ❌ {language}: Error ({str(e)})")
            all_successful = False
    
    return all_successful

def test_web_interface():
    """Test web interface accessibility"""
    print("\n🌐 Testing Web Interface...")
    
    try:
        response = requests.get(CLIENT_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print("  ✅ Web interface: Accessible")
            return True
        else:
            print(f"  ❌ Web interface: Not accessible (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"  ❌ Web interface: Error ({str(e)})")
        return False

def test_file_upload():
    """Test file upload functionality"""
    print("\n📁 Testing File Upload...")
    
    # Create a simple test file content
    test_content = 'print("Test file upload")'
    
    try:
        files = {'code': ('test.py', test_content, 'text/plain')}
        response = requests.post(f"{ROUTER_URL}/upload", files=files, timeout=TIMEOUT)
        
        if response.status_code == 200:
            result = response.json()
            print(f"  ✅ File upload: Success (File ID: {result.get('file_id', 'N/A')})")
            return True
        else:
            print(f"  ❌ File upload: Failed (Status: {response.status_code})")
            print(f"      Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"  ❌ File upload: Error ({str(e)})")
        return False

def main():
    """Main test function"""
    print("🧪 Multi-Language Code Execution System - Test Suite")
    print("=" * 60)
    
    # Wait a bit for services to start
    print("⏳ Waiting for services to start...")
    time.sleep(5)
    
    # Run all tests
    tests = [
        ("Health Endpoints", test_health_endpoints),
        ("Code Execution", test_code_execution),
        ("Web Interface", test_web_interface),
        ("File Upload", test_file_upload)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name}: Test failed with exception: {str(e)}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the services.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 