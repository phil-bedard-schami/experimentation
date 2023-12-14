import os
import subprocess

# Prerequisites (git, pandoc, python)

# Configurations
git_repo_url = 'https://github.com/username/repo.git'  # Replace with your repository URL
folder_path = 'path/to/folder'  # Folder path inside the repo
output_md = 'combined.md'  # Temporary combined Markdown file
output_pdf = 'output.pdf'  # Final PDF file name
exclude_file = 'README.md'  # File to exclude from compilation

# Clone the GitHub repository
subprocess.run(['git', 'clone', git_repo_url, 'repo'])
os.chdir('repo')

# Combine Markdown files
with open(output_md, 'w') as outfile:
    for md_file in os.listdir(folder_path):
        if md_file.endswith('.md') and md_file != exclude_file:
            with open(os.path.join(folder_path, md_file), 'r') as infile:
                outfile.write(infile.read() + '\n\n')

# Convert to PDF using Pandoc
subprocess.run(['pandoc', output_md, '-o', output_pdf])

# Clean up (optional)
os.remove(output_md)
os.chdir('..')
subprocess.run(['rm', '-rf', 'repo'])

print(f'PDF generated: {output_pdf}')