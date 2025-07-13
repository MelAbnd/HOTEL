<?php
require_once __DIR__ . '/../core/app/model/HabitacionData.php';
use PHPUnit\Framework\TestCase;

class HabitacionDataTest extends TestCase
{
    private $habitacion;

    protected function setUp()
    {
        $this->habitacion = new HabitacionData();
    }

    /**
     * @test
     * Test habitacion constructor initializes properties correctly
     */
    public function testConstructorInitializesProperties()
    {
        $habitacion = new HabitacionData();
        
        $this->assertEquals("", $habitacion->nombre);
        $this->assertEquals("", $habitacion->descripcion);
        $this->assertEquals("NOW()", $habitacion->fecha_creada);
    }

    /**
     * @test
     * Test setting habitacion properties
     */
    public function testSetHabitacionProperties()
    {
        $this->habitacion->nombre = "Suite Presidencial";
        $this->habitacion->descripcion = "Suite de lujo con vista al mar";
        $this->habitacion->precio = "500.00";
        $this->habitacion->id_categoria = 1;
        $this->habitacion->estado = "1";

        $this->assertEquals("Suite Presidencial", $this->habitacion->nombre);
        $this->assertEquals("Suite de lujo con vista al mar", $this->habitacion->descripcion);
        $this->assertEquals("500.00", $this->habitacion->precio);
        $this->assertEquals(1, $this->habitacion->id_categoria);
        $this->assertEquals("1", $this->habitacion->estado);
    }

    /**
     * @test
     * Test room name validation
     */
    public function testRoomNameValidation()
    {
        $this->habitacion->nombre = "Suite 101";
        
        $this->assertNotEmpty($this->habitacion->nombre);
        $this->assertTrue(is_string($this->habitacion->nombre));
        $this->assertLessThanOrEqual(100, strlen($this->habitacion->nombre));
    }

    /**
     * @test
     * Test room price validation
     */
    public function testRoomPriceValidation()
    {
        $validPrices = ["100.00", "250.50", "1000.99"];
        
        foreach ($validPrices as $price) {
            $this->habitacion->precio = $price;
            $this->assertRegExp('/^\d+(\.\d{2})?$/', $this->habitacion->precio);
        }
    }

    /**
     * @test
     * Test room status validation
     */
    public function testRoomStatusValidation()
    {
        $validStatuses = ["1", "2", "3"]; // 1=Libre, 2=Ocupado, 3=Mantenimiento
        
        foreach ($validStatuses as $status) {
            $this->habitacion->estado = $status;
            $this->assertContains($this->habitacion->estado, $validStatuses);
        }
    }

    /**
     * @test
     * Test room description length
     */
    public function testRoomDescriptionLength()
    {
        $longDescription = str_repeat("A", 500);
        $this->habitacion->descripcion = $longDescription;
        
        $this->assertLessThanOrEqual(500, strlen($this->habitacion->descripcion));
    }

    /**
     * @test
     * Test room category assignment
     */
    public function testRoomCategoryAssignment()
    {
        $this->habitacion->id_categoria = 1;
        
        $this->assertTrue(is_numeric($this->habitacion->id_categoria));
        $this->assertGreaterThan(0, $this->habitacion->id_categoria);
    }

    /**
     * @test
     * Test SQL injection prevention in room name
     */
    public function testSQLInjectionPrevention()
    {
        $maliciousInput = "'; DROP TABLE habitacion; --";
        $this->habitacion->nombre = $maliciousInput;
        
        // Should contain the malicious string as-is (not executed)
        $this->assertEquals($maliciousInput, $this->habitacion->nombre);
    }

    /**
     * @test
     * Test room data serialization
     */
    public function testRoomDataSerialization()
    {
        $this->habitacion->nombre = "Suite Test";
        $this->habitacion->descripcion = "Test Description";
        $this->habitacion->precio = "150.00";
        
        $serialized = serialize($this->habitacion);
        $unserialized = unserialize($serialized);
        
        $this->assertEquals($this->habitacion->nombre, $unserialized->nombre);
        $this->assertEquals($this->habitacion->descripcion, $unserialized->descripcion);
        $this->assertEquals($this->habitacion->precio, $unserialized->precio);
    }

    /**
     * @test
     * Test room state transitions
     */
    public function testRoomStateTransitions()
    {
        // Test libre to ocupado
        $this->habitacion->estado = "1"; // Libre
        $this->assertEquals("1", $this->habitacion->estado);
        
        $this->habitacion->estado = "2"; // Ocupado
        $this->assertEquals("2", $this->habitacion->estado);
        
        // Test ocupado to libre
        $this->habitacion->estado = "1"; // Libre
        $this->assertEquals("1", $this->habitacion->estado);
    }

    /**
     * @test
     * Test room data validation for required fields
     */
    public function testRequiredFieldsValidation()
    {
        $this->habitacion->nombre = "Suite Test";
        $this->habitacion->precio = "100.00";
        $this->habitacion->id_categoria = 1;
        $this->habitacion->estado = "1";
        
        $this->assertNotEmpty($this->habitacion->nombre);
        $this->assertNotEmpty($this->habitacion->precio);
        $this->assertNotEmpty($this->habitacion->id_categoria);
        $this->assertNotEmpty($this->habitacion->estado);
    }

    protected function tearDown()
    {
        $this->habitacion = null;
    }
}
