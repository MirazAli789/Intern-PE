#!/usr/bin/env python3
"""
Test script for Connect Four games
"""

import sys
import subprocess
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        # Test pygame import
        import pygame
        print("✓ pygame imported successfully")
        
        # Test basic Python modules
        import math
        print("✓ math module imported successfully")
        
        # Test CLI version import
        from connect_four_cli import ConnectFourCLI
        print("✓ CLI version imported successfully")
        
        # Test GUI version import
        from connect_four import ConnectFour
        print("✓ GUI version imported successfully")
        
        print("\n✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_cli_game():
    """Test basic functionality of CLI game"""
    print("\nTesting CLI game basic functionality...")
    
    try:
        from connect_four_cli import ConnectFourCLI
        game = ConnectFourCLI()
        
        # Test board initialization
        assert game.rows == 6
        assert game.cols == 7
        assert game.current_player == 1
        print("✓ Board initialization works")
        
        # Test valid move checking
        assert game.is_valid_move(0) == True
        assert game.is_valid_move(6) == True
        assert game.is_valid_move(-1) == False
        assert game.is_valid_move(7) == False
        print("✓ Move validation works")
        
        # Test making a move
        assert game.make_move(0, 1) == True
        assert game.board[0][0] == 1
        print("✓ Making moves works")
        
        print("✅ CLI game basic functionality test passed!")
        return True
        
    except Exception as e:
        print(f"❌ CLI game test failed: {e}")
        return False

def test_gui_game():
    """Test basic functionality of GUI game"""
    print("\nTesting GUI game basic functionality...")
    
    try:
        # Import pygame without initializing display
        import pygame
        pygame.init()
        
        from connect_four import ConnectFour
        
        # Test basic initialization (without creating display)
        game = ConnectFour()
        
        # Test board initialization
        assert len(game.board) == 6
        assert len(game.board[0]) == 7
        assert game.current_player == 1
        print("✓ Board initialization works")
        
        # Test valid location checking
        assert game.is_valid_location(0) == True
        assert game.is_valid_location(6) == True
        print("✓ Location validation works")
        
        # Test getting next open row
        row = game.get_next_open_row(0)
        assert row == 0
        print("✓ Row finding works")
        
        # Test dropping piece
        game.drop_piece(0, 0, 1)
        assert game.board[0][0] == 1
        print("✓ Piece dropping works")
        
        pygame.quit()
        print("✅ GUI game basic functionality test passed!")
        return True
        
    except Exception as e:
        print(f"❌ GUI game test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running Connect Four Game Tests\n")
    
    tests_passed = 0
    total_tests = 3
    
    if test_imports():
        tests_passed += 1
    
    if test_cli_game():
        tests_passed += 1
        
    if test_gui_game():
        tests_passed += 1
    
    print(f"\n📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your Connect Four games are ready to play!")
        print("\n🎮 How to run:")
        print("   For GUI version: python connect_four.py")
        print("   For CLI version: python connect_four_cli.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
