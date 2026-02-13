import xml.etree.ElementTree as ET
import os

report_path = 'tests/build/reports/jacoco/test/jacocoTestReport.xml'

if not os.path.exists(report_path):
    print(f"Report not found at {report_path}")
    exit(1)

tree = ET.parse(report_path)
root = tree.getroot()

missed_branches = []

for package in root.findall('package'):
    package_name = package.get('name')
    for sourcefile in package.findall('sourcefile'):
        filename = sourcefile.get('name')
        for counter in sourcefile.findall('counter'):
            if counter.get('type') == 'BRANCH':
                missed = int(counter.get('missed'))
                covered = int(counter.get('covered'))
                total = missed + covered
                if total > 0:
                    missed_branches.append({
                        'package': package_name,
                        'file': filename,
                        'missed': missed,
                        'covered': covered,
                        'total': total,
                        'percentage': (covered / total) * 100
                    })

# Sort by missed branches descending
missed_branches.sort(key=lambda x: x['missed'], reverse=True)

print(f"{'File':<40} | {'Missed':<10} | {'Covered':<10} | {'Total':<10} | {'Coverage %':<10}")
print("-" * 90)
for item in missed_branches[:20]:
    print(f"{item['file']:<40} | {item['missed']:<10} | {item['covered']:<10} | {item['total']:<10} | {item['percentage']:.2f}%")
