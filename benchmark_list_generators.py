"""
Démonstration comparative : Générateurs vs Listes
Installation requise : pip install memory-profiler psutil
"""
import time
import psutil
import os
from memory_profiler import profile

def get_memory_usage():
    """Retourne l'usage mémoire actuel en MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

# Approche traditionnelle avec liste
@profile
def process_data_list(n):
    # Crée une liste complète en mémoire
    return [i * i for i in range(n)]

# Approche avec générateur
@profile
def process_data_generator(n):
    # Génère les valeurs une par une
    for i in range(n):
        yield i * i

def compare_performance(n=10_000_000):
    # Test avec liste
    start_time = time.time()
    start_mem = get_memory_usage()
    
    list_result = process_data_list(n)
    # Force l'évaluation complète
    sum(list_result)  
    
    list_time = time.time() - start_time
    list_mem = get_memory_usage() - start_mem

    # Nettoyage mémoire
    list_result = None
    
    # Test avec générateur
    start_time = time.time()
    start_mem = get_memory_usage()
    
    gen_result = process_data_generator(n)
    # Force l'évaluation complète
    sum(gen_result)  
    
    gen_time = time.time() - start_time
    gen_mem = get_memory_usage() - start_mem

    print(f"\nComparaison pour {n:,} éléments:")
    print(f"\nApproche traditionnelle (liste):")
    print(f"Temps d'exécution: {list_time:.2f} secondes")
    print(f"Utilisation mémoire: {list_mem:.2f} MB")
    
    print(f"\nApproche avec générateur:")
    print(f"Temps d'exécution: {gen_time:.2f} secondes")
    print(f"Utilisation mémoire: {gen_mem:.2f} MB")
    
    print(f"\nRatio d'amélioration:")
    print(f"Temps: {list_time/gen_time:.1f}x plus rapide")
    # J'ajoute 0.001 d'utilisation RAM pour ne pas avoir de divison par 0
    print(f"Mémoire: {list_mem/(gen_mem+0.001):.1f}x moins de mémoire")

if __name__ == "__main__":
    # Exemple avec un cas plus réaliste
    def read_huge_file():
        """Simulation de lecture d'un gros fichier"""
        # Version avec liste
        def traditional():
            return [f"ligne_{i}" for i in range(1_000_000)]
            
        # Version avec générateur
        def with_generator():
            for i in range(1_000_000):
                yield f"ligne_{i}"
                
        # Comparaison
        print("\nTest de lecture d'un gros fichier:")
        
        start = time.time()
        lines = traditional()
        for line in lines: pass
        print(f"Temps version traditionnelle: {time.time() - start:.2f}s")
        
        start = time.time()
        for line in with_generator(): pass
        print(f"Temps version générateur: {time.time() - start:.2f}s")
    
    # Lance les tests
    compare_performance()
    read_huge_file()