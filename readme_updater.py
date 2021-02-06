import leetcode_table_maker as table_gen
import contribute_point_calculator as point_calc

readme_template = None
with open("./README-Template.md", "r") as readme_file:
    readme_template = readme_file.read()

readme_template = readme_template.replace("{ranking}", point_calc.get_contents())
readme_template = readme_template.replace("{tables}", table_gen.get_contents())

with open("./README.md", "w") as readme_file:
    readme_file.write(readme_template)