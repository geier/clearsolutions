from nbconvert.preprocessors.base import Preprocessor


class ClearSolutionsPreprocessor(Preprocessor):

    def preprocess_cell(self, cell, resources, index):
        if 'solution' in cell.metadata.get('tags', []):
            cell['source'] = []
            cell['outputs'] = []
            cell['execution_count'] = None
        return cell, resources
