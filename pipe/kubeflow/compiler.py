from kfp import compiler
from sample_pipeline import hello_pipeline

compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')

