class Ontology:

    def __init__(self):
        self.ontology = {
            'Top': {
                'science': {
                    'computer science': {
                        'robotics': {
                            'planning': {
                                'topic_words': ['planning', 'd*', 'path', 'real-time', 'trajectories', 'algorithms',
                                                'efficient', 'map', 'robotics', 'solution', 'models', 'hard',
                                                'navigation', 'complexity'],
                                'talks': list()  # to add
                            },
                            'robot motion': {
                                'topic_words': ['locomotion', 'robotics', 'sensors', 'walking', 'leg', 'terrain',
                                                'range', 'recovery', 'planning', 'control', 'trajectory', 'dexterous',
                                                'learning', 'control', 'running', 'mobile', 'explore', 'gait',
                                                'exploration', 'arm'],
                                'talks': list()  # to add
                            },
                            'robotics learning': {
                                'topic_words': ['training', 'robot', 'learning', 'data', 'performance', 'intelligence',
                                                'skill', 'goal', 'gradient', 'descent', 'sensor'],
                                'talks': list()  # to add
                            },
                            'medical robotics': {
                                'topic_words': ['robotics', 'medicine', 'anatomy', 'surgeon', 'precision', 'bone',
                                                'accuracy', 'implant', 'surgery', 'medical'],
                                'talks': list()  # to add
                            },
                            'space robots': {
                                'topic_words': ['robotics', 'space', 'missions', 'center', 'nasa', 'international',
                                                'station', 'payload', 'astronaut'],
                                'talks': list()  # to add
                            },
                            'topic_words': ['robot', 'scheduling', 'asynchronous', 'locomotion', 'sensors',
                                            'autonomous', 'assistance', 'machine', 'control', 'feedback', 'control',
                                            'actuator', 'sensor', 'research', 'task'],
                            'talks': list()  # to add
                        },
                        'vision': {
                            'topic_words': ['vision', 'magnification', 'optical', 'focus', 'dimension', 'image',
                                            'tracking', 'object', 'transformation', 'visual', 'pattern', 'sensor',
                                            'range', 'photogrammetric', 'maps', 'geometric', 'measure', 'structure',
                                            'sensing'],
                            'talks': list()  # to add
                        },
                        'graphics': {
                            'topic_words': ['graphics', 'display', 'image', '3d', 'vision', 'screen', 'resolution',
                                            'compression', 'art', 'color', 'colour', 'visualization', 'resampling',
                                            'raster', 'rotation', 'photo', 'drawing', 'video', 'fidelity', 'frame'],
                            'talks': list()  # to add
                        },
                        'programming': {
                            'topic_words': ['programming', 'language', 'parallel', 'object', 'oriented', 'memory',
                                            'low', 'high', 'level', 'deadlock', 'classes', 'data', 'structures',
                                            'code', 'system', 'compiler', 'functional', 'testing', 'class',
                                            'breakpoint', 'executing', 'fortran', 'prototype', 'typed', 'variable',
                                            'garbage', 'collect'],
                            'talks': list()  # to add
                        },
                        'nlp': {
                            'topic_words': ['language', 'syntax', 'semantics', 'pragmatics', 'meaning', 'comprehension',
                                            'nlp', 'nl', 'recognition', 'knowledge', 'internet', 'information',
                                            'translation', 'lexical', 'speech', 'speaking', 'synthesis', 'sentence',
                                            'recognition', 'grammar'],
                            'talks': list()  # to add
                        },
                        'machine learning': {
                            'topic_words': ['learning', 'autonomous', 'classifier', 'categorizing', 'data',
                                            'knowledge', 'neural', 'bayesian', 'forest', 'perception', 'model',
                                            'network', 'combinatorics', 'ambiguity', 'vector', 'pattern', 'neuron',
                                            'intelligence', 'minimax', 'tree', 'ai', 'classification', 'linear',
                                            'planning', 'unforeseen', 'artificial'],
                            'talks': list()  # to add
                        },
                        'computer architecture': {
                            'topic_words': ['architecture', 'computer', 'i/o', 'io', 'processor', 'memory', 'threads',
                                            'efficiency', 'cache', 'model', 'parallel', 'disk', 'workstation',
                                            'multiprocessor', 'hardware', 'controller', 'network', 'supercomputer',
                                            'physical', 'environment', 'structure', 'level', 'system',
                                            'multiprocessors', 'dram'],
                            'talks': list()  # to add
                        },
                        'logic and reasoning': {
                            'topic_words': ['logic', 'reasoning', 'probability', 'probabilistic', 'semantics',
                                            'algorithm', 'decision', 'language', 'rules', 'philosophy', 'automated',
                                            'paramodulation', 'math', 'classical', 'true', 'false', 'theory',
                                            'monotonic', 'automata', 'finite', 'state', 'machine'],
                            'talks': list()  # to add
                        },
                        'control systems': {
                            'topic_words': ['control', 'system', 'operation', 'assembly', 'maintenance', 'servicing',
                                            'ics', 'industry', 'operate', 'technical', 'task', 'scheduling',
                                            'settings'],
                            'talks': list()  # to add
                        },
                        'topic_words': ['cs', 'computer', 'science', 'agent', 'application', 'problem', 'solution',
                                        'program', 'efficiency', 'automatic', 'data', 'speed', 'device',
                                        'computing', 'apple', 'technology', 'time', 'graph', 'user', 'interface',
                                        'hewlett', 'packard', 'internet', 'email', 'information', 'programmer',
                                        'system'],
                        'talks': list()  # to add
                    },
                    'engineering': {
                        'magnetic and electric materials': {
                            'topic_words': ['electricity', 'magnets', 'micron', 'silicon', 'strength', 'energy',
                                            'interconnected', 'waveform', 'circuit', 'positive'],
                            'talks': list()  # to add
                        },
                        'manufacturing': {
                            'topic_words': ['manufacturing', 'build', 'engineering', 'industry', 'technology',
                                            'control', 'welding', 'part', 'product' 'requirements', 'automated',
                                            'force'],
                            'talks': list()  # to add
                        },
                        'design': {
                            'topic_words': ['product', 'design', 'engineer', 'recycle', 'waste', 'productivity',
                                            'process', 'life', 'cycle', 'analysis', 'part', 'forces', 'simulation',
                                            'force', 'green', 'enviroment'],
                            'talks': list()  # to add
                        },
                        'policy': {
                            'topic_words': ['residential', 'policy', 'public', 'engineering', 'garbage', 'household',
                                            'pricing', 'legal', 'illegal'],
                            'talks': list()  # to add
                        },
                        'topic_words': ['engineering', 'tool', 'fourier', 'physics', 'problem', 'algebra',
                                        'kinematics', 'laboratory', 'laser', 'semiconductor', 'molecules', 'structure',
                                        'biomolecules', 'bio', 'biomechanics'],
                        'talks': list()  # to add
                    },
                    'mathematics': {
                        'geometry': {
                            'topic_words': ['mathematics', 'geometry', 'linear', 'length', 'shape', 'solid',
                                            'interpolation', 'space'],
                            'talks': list()  # to add
                        },
                        'topic_words': ['math', 'mathematics', 'functions', 'parametric', 'curve',
                                        'algorithms', 'polynomial', 'gaussian', 'theory', 'power', 'graph', 'root',
                                        'square', 'cycles'],
                        'talks': list()  # to add
                    },
                },
                'teaching': {
                    'topic_words': ['teaching', 'support', 'ta', 'academic', 'coach', 'class', 'classroom',
                                    'group', 'lecture', 'academic', 'planning', 'course', 'group', 'professor',
                                    'education'],
                    'talks': list()  # to add
                },
                'student and working life': {
                    'topic_words': ['student', 'aid', 'graduate', 'loan', 'application', 'tax', 'income', 'health',
                                    'office'],
                    'talks': list()  # to add
                },
            }
        }
        self.traversal_info = dict()
        self.traverse()

    def traverse(self):
        depth_one = self.ontology["Top"].keys()

        for depth_one_key in depth_one:
            depth_two = self.ontology["Top"][depth_one_key].keys()

            if "topic_words" in depth_two:
                self.traversal_info[depth_one_key] = (
                    ["Top", depth_one_key], self.ontology["Top"][depth_one_key]["topic_words"])

            for depth_two_key in depth_two:

                if depth_two_key not in ["topic_words", "talks"]:

                    depth_three = self.ontology["Top"][depth_one_key][depth_two_key].keys()

                    if "topic_words" in depth_three:
                        self.traversal_info[depth_two_key] = (
                            ["Top", depth_one_key, depth_two_key], self.ontology["Top"][depth_one_key][depth_two_key][
                                "topic_words"])

                    for depth_three_key in depth_three:

                        if depth_three_key not in ["topic_words", "talks"]:

                            depth_four = self.ontology["Top"][depth_one_key][depth_two_key][depth_three_key].keys()

                            if "topic_words" in depth_four:
                                self.traversal_info[depth_three_key] = (["Top", depth_one_key, depth_two_key,
                                                                         depth_three_key],
                                                                        self.ontology["Top"][depth_one_key][
                                                                            depth_two_key][
                                                                            depth_three_key]["topic_words"])

                            for depth_four_key in depth_four:
                                if depth_four_key not in ["topic_words", "talks"]:
                                    self.traversal_info[depth_four_key] = (["Top", depth_one_key, depth_two_key,
                                                                            depth_three_key, depth_four_key],
                                                                           self.ontology["Top"][depth_one_key][
                                                                               depth_two_key][depth_three_key][
                                                                               depth_four_key]["topic_words"])

    def add_email(self, topic, file_name):
        location = self.traversal_info[topic][0]

        if len(location) == 2:
            self.ontology["Top"][location[1]]["talks"].append(file_name)
        elif len(location) == 3:
            self.ontology["Top"][location[1]][location[2]]["talks"].append(file_name)
        elif len(location) == 4:
            self.ontology["Top"][location[1]][location[2]][location[3]]["talks"].append(file_name)
        elif len(location) == 5:
            self.ontology["Top"][location[1]][location[2]][location[3]][location[4]]["talks"].append(file_name)

    def __str__(self):
        string = "Ontology: \n\n Top"

        depth_one = self.ontology['Top'].keys()

        for depth_one_key in depth_one:
            string += "\n|---- " + depth_one_key
            depth_two = self.ontology['Top'][depth_one_key].keys()

            if "topic_words" in depth_two:
                talks = self.ontology['Top'][depth_one_key]['talks']
                if len(talks) > 0:
                    string += "\n|       |---- file names:"

                for talk in talks:
                    string += "\n|       |       |---- " + talk

            for depth_two_key in depth_two:
                if depth_two_key not in ["topic_words", "talks"]:
                    string += "\n|      |---- " + depth_two_key

                    depth_three = self.ontology['Top'][depth_one_key][depth_two_key].keys()

                    if "topic_words" in depth_three:
                        talks = self.ontology['Top'][depth_one_key][depth_two_key]['talks']
                        if len(talks) > 0:
                            string += "\n|      |       |---- file names:"

                        for talk in talks:
                            string += "\n|      |       |       |---- " + talk

                    for depth_three_key in depth_three:
                        if depth_three_key not in ["topic_words", "talks"]:
                            string += "\n|      |       |---- " + depth_three_key
                            depth_four = self.ontology['Top'][depth_one_key][depth_two_key][depth_three_key].keys()
                            if "topic_words" in depth_four:
                                talks = self.ontology['Top'][depth_one_key][depth_two_key][depth_three_key]['talks']
                                if len(talks) > 0:
                                    string += "\n|      |       |       |---- file names:"

                                for talk in talks:
                                    string += "\n|      |       |       |      |---- " + talk

                            for depth_four_key in depth_four:
                                if depth_four_key not in ["topic_words", "talks"]:
                                    string += "\n|      |       |       |---- " + depth_four_key

                                    talks = \
                                        self.ontology['Top'][depth_one_key][depth_two_key][depth_three_key][
                                            depth_four_key][
                                            'talks']
                                    if len(talks) > 0:
                                        string += "\n|      |       |       |       |---- file names:"

                                    for talk in talks:
                                        string += "\n|      |       |       |       |      |---- " + talk
        return string
