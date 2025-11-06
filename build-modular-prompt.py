#!/usr/bin/env python3
"""
Modular Prompt Assembly Script

This script combines modular prompt components into a final agent prompt file.
It reads a template file with component references and replaces them with
the actual content from component files.

Usage:
    python build-modular-prompt.py <agent-name> [options]

Arguments:
    agent-name          Name of the agent folder (e.g., web-search-agent, data-processor)

Options:
    --template FILE     Template file with references (default: agent_prompt_modular.xml)
    --output FILE       Output file for assembled prompt (default: agent_prompt.xml)
    --parts-dir DIR     Directory containing component files (default: prompt-parts)
    --validate          Validate XML syntax after assembly
    --verbose           Show detailed processing information

Examples:
    python build-modular-prompt.py web-search-agent
    python build-modular-prompt.py data-processor --validate --verbose
    python build-modular-prompt.py web-search-agent --template custom_template.xml
"""

import os
import re
import sys
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Tuple


class ModularPromptBuilder:
    """Builds final agent prompts from modular components."""
    
    def __init__(self, agent_name: str, template_file: str, output_file: str, parts_dir: str, verbose: bool = False):
        # Build paths relative to the agent directory
        self.agent_dir = Path("modules") / agent_name
        self.template_file = self.agent_dir / template_file
        self.output_file = self.agent_dir / output_file
        self.parts_dir = self.agent_dir / parts_dir
        self.verbose = verbose
        
        # Reference pattern: <!-- REFERENCE: path/to/file.xml -->
        # Description pattern: <!-- Description of component -->
        self.reference_pattern = re.compile(
            r'<!-- REFERENCE: ([^>]+) -->\s*<!-- ([^>]+) -->',
            re.MULTILINE | re.DOTALL
        )
    
    def log(self, message: str) -> None:
        """Log message if verbose mode is enabled."""
        if self.verbose:
            print(f"[BUILD] {message}")
    
    def read_component(self, component_path: str) -> Tuple[str, bool]:
        """
        Read component file and return content with XML declaration removed.
        
        Args:
            component_path: Relative path to component file
            
        Returns:
            Tuple of (content, success_flag)
        """
        # Remove parts-dir prefix if it's already in the component_path
        if component_path.startswith(self.parts_dir.name + "/"):
            component_path = component_path[len(self.parts_dir.name) + 1:]
        
        full_path = self.parts_dir / component_path
        
        if not full_path.exists():
            error_msg = f"ERROR: Component file not found: {full_path}"
            self.log(error_msg)
            return f"<!-- {error_msg} -->", False
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove XML declaration from component files
            lines = content.split('\n')
            if lines and lines[0].strip().startswith('<?xml'):
                content = '\n'.join(lines[1:])
            
            self.log(f"Successfully read component: {component_path}")
            return content, True
            
        except Exception as e:
            error_msg = f"ERROR: Failed to read {component_path}: {str(e)}"
            self.log(error_msg)
            return f"<!-- {error_msg} -->", False
    
    def replace_reference(self, match: re.Match) -> str:
        """
        Replace a single reference with component content.
        
        Args:
            match: Regex match object containing reference and description
            
        Returns:
            Replacement text with component content
        """
        component_path = match.group(1).strip()
        description = match.group(2).strip()
        
        self.log(f"Processing reference: {component_path}")
        
        # Read component content
        content, success = self.read_component(component_path)
        
        # Build replacement text
        replacement = f"<!-- {description} -->\n"
        replacement += f"<!-- SOURCE: {component_path} -->\n"
        replacement += content
        
        return replacement
    
    def validate_xml(self, content: str) -> Tuple[bool, Optional[str]]:
        """
        Validate XML syntax of the assembled content.
        
        Args:
            content: XML content to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            ET.fromstring(content)
            return True, None
        except ET.ParseError as e:
            return False, str(e)
    
    def build(self, validate: bool = False) -> bool:
        """
        Build the final prompt from template and components.
        
        Args:
            validate: Whether to validate XML syntax after assembly
            
        Returns:
            True if build was successful, False otherwise
        """
        # Check if template file exists
        if not self.template_file.exists():
            print(f"ERROR: Template file not found: {self.template_file}")
            return False
        
        # Check if parts directory exists
        if not self.parts_dir.exists():
            print(f"ERROR: Parts directory not found: {self.parts_dir}")
            return False
        
        self.log(f"Reading template: {self.template_file}")
        
        # Read template content
        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()
        except Exception as e:
            print(f"ERROR: Failed to read template file: {str(e)}")
            return False
        
        # Find and count references
        references = self.reference_pattern.findall(template_content)
        self.log(f"Found {len(references)} component references")
        
        if not references:
            print("WARNING: No component references found in template")
        
        # Replace all references with component content
        final_content = self.reference_pattern.sub(self.replace_reference, template_content)
        
        # Validate XML if requested
        if validate:
            self.log("Validating XML syntax...")
            is_valid, error_msg = self.validate_xml(final_content)
            if not is_valid:
                print(f"ERROR: XML validation failed: {error_msg}")
                return False
            self.log("XML validation passed")
        
        # Write final content
        try:
            # Ensure output directory exists
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            self.log(f"Successfully wrote final prompt: {self.output_file}")
            return True
            
        except Exception as e:
            print(f"ERROR: Failed to write output file: {str(e)}")
            return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Build final agent prompt from modular components",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build-modular-prompt.py web-search-agent
  python build-modular-prompt.py data-processor --validate --verbose
  python build-modular-prompt.py web-search-agent --template custom_template.xml
        """
    )
    
    parser.add_argument(
        'agent_name',
        help='Name of the agent folder (e.g., web-search-agent, data-processor)'
    )
    
    parser.add_argument(
        '--template',
        default='agent_prompt_modular.xml',
        help='Template file with component references (default: agent_prompt_modular.xml)'
    )
    
    parser.add_argument(
        '--output',
        default='agent_prompt.xml',
        help='Output file for assembled prompt (default: agent_prompt.xml)'
    )
    
    parser.add_argument(
        '--parts-dir',
        default='prompt-parts',
        help='Directory containing component files (default: prompt-parts)'
    )
    
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate XML syntax after assembly'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed processing information'
    )
    
    args = parser.parse_args()
    
    # Create builder instance
    builder = ModularPromptBuilder(
        agent_name=args.agent_name,
        template_file=args.template,
        output_file=args.output,
        parts_dir=args.parts_dir,
        verbose=args.verbose
    )
    
    # Build the prompt
    print(f"Building modular prompt for agent: {args.agent_name}")
    print(f"  Template: {args.template}")
    print(f"  Output: {args.output}")
    print(f"  Parts Directory: {args.parts_dir}")
    
    success = builder.build(validate=args.validate)
    
    if success:
        print("✓ Build completed successfully!")
        
        # Show final stats
        output_path = Path("modules") / args.agent_name / args.output
        if output_path.exists():
            size = output_path.stat().st_size
            print(f"  Final prompt size: {size:,} bytes")
    else:
        print("✗ Build failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()